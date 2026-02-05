def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {"orders": {}, "last_checked": None}


def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def fetch_recent_orders(side='buy,sell', status='all', pages=3, page_size=200, order_count=None):
    """
    Fetch orders with pagination.
    
    - Max 200 orders per page
    - Keeps fetching until API returns empty list
    - If order_count is provided, stops after collecting that many orders
    """
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders"
    currency = 'INR'
    # 
    if status == 'all':
        status = (
            'open,filled,partially_filled,partially_cancelled,'
            'cancelled,rejected,untriggered'
        )
    # 
    all_orders = []
    # 
    for page in range(1, pages + 1):
        body = {
            "timestamp": generate_timestamp(),
            "status": status,
            "side": side,
            "page": str(page),
            "size": str(page_size),
            "margin_currency_short_name": [currency],
        }
        headers, json_body = generate_headers_and_body(body)
        orders = safe_post(url, headers, json_body)
        # 
        if not orders:
            break
        # 
        all_orders.extend(orders)
        # 
        # Stop if order_count reached
        if order_count is not None and len(all_orders) >= order_count:
            all_orders = all_orders[:order_count]
            break
        # 
        time.sleep(RATE_LIMIT_DELAY)
    # 
    return pd.DataFrame(all_orders)


def detect_order_updates(orderDF, cache):
    """
    Returns:
      - new_or_updated_orders (DataFrame)
      - updated cache
    """
    if orderDF.empty:
        return orderDF, cache
    # 
    orderDF = orderDF.copy()
    orderDF['updated_at'] = epoch_to_datetime(orderDF['updated_at'])
    # 
    updated_rows = []
    # 
    for _, row in orderDF.iterrows():
        oid = row['id']
        updated_at = row['updated_at'].isoformat()
        status = row['status']
        # 
        cached = cache["orders"].get(oid)
        # 
        if (
            cached is None or
            cached["status"] != status or
            cached["updated_at"] != updated_at
        ):
            updated_rows.append(row)
            # 
            cache["orders"][oid] = {
                "status": status,
                "updated_at": updated_at
            }
    # 
    cache["last_checked"] = datetime.utcnow().isoformat()
    return pd.DataFrame(updated_rows), cache


def fetch_orders_with_cache():
    cache = load_cache()
    orderDF = fetch_recent_orders(pages=1)
    updatedDF, cache = detect_order_updates(orderDF, cache)
    save_cache(cache)
    return updatedDF




def place_buy_for_filled_sells(filled_sells_df, all_orders_df, pair, step, place_buy_order,):
    """
    For every FILLED SELL, re-enter BUY at -1 grid
    if it does not already exist.
    """
    if filled_sells_df.empty:
        return
    # 
    buys = all_orders_df[
        (all_orders_df['pair'] == pair) &
        (all_orders_df['side'] == 'buy') &
        (all_orders_df['status'] == 'open')
    ]
    # 
    existing_buy_grids = {
        price_to_grid(p, step)
        for p in buys['price']
    }
    # 
    for _, sell in filled_sells_df.iterrows():
        sell_grid = price_to_grid(sell['price'], step)
        buy_grid = sell_grid - 1
        # 
        if buy_grid in existing_buy_grids:
            continue  # BUY already exists
        # 
        buy_price = grid_to_price(buy_grid, step)
        place_buy_order(pair=pair, price=buy_price)


def split_filled_orders(updated_orders_df, pair):
    """
    Only act on newly updated orders, not all history.

    Splits updated orders into:
    - newly filled BUYs
    - newly filled SELLs
    """
    # 
    filled_buys = updated_orders_df[
        (updated_orders_df['pair'] == pair) &
        (updated_orders_df['side'] == 'buy') &
        (updated_orders_df['status'] == 'filled')
    ]
    # 
    filled_sells = updated_orders_df[
        (updated_orders_df['pair'] == pair) &
        (updated_orders_df['side'] == 'sell') &
        (updated_orders_df['status'] == 'filled')
    ]
    # 
    return filled_buys, filled_sells


def run_grid_cycle(
    updated_orders_df,
    full_order_df,
    pair,
    ltp,
    open_trade_count,
    step,
    place_buy_order,
    place_sell_order,
):
    # A️⃣ Maintain BUY grid below LTP
    maintain_buy_grid(
        orderDF=full_order_df,
        pair=pair,
        ltp=ltp,
        open_trade_count=open_trade_count,
        step_price_diff=step,
        place_buy_order=place_buy_order,
    )

    # B️⃣ Detect filled orders from updates
    filled_buys, filled_sells = split_filled_orders(
        updated_orders_df,
        pair
    )

    # C️⃣ BUY filled → SELL
    place_sell_for_filled_buys(
        filled_buys_df=filled_buys,
        all_orders_df=full_order_df,
        pair=pair,
        step=step,
        place_sell_order=place_sell_order,
    )

    # D️⃣ SELL filled → BUY
    place_buy_for_filled_sells(
        filled_sells_df=filled_sells,
        all_orders_df=full_order_df,
        pair=pair,
        step=step,
        place_buy_order=place_buy_order,
    )


# # --------------------------------------------------------------------------------------------------

def split_orders_by_symbol(orderDF):
    return {
        pair: df.copy()
        for pair, df in orderDF.groupby('pair')
    }


def get_updated_orders(orderDF, last_seen):
    if last_seen is None:
        return orderDF
    return orderDF[orderDF['updated_at'] > last_seen]


def run_symbol_grid(
    pair,
    config,
    symbol_orders_df,
    updated_orders_df,
    ltp
    ):
    run_grid_cycle(
        updated_orders_df=updated_orders_df,
        full_order_df=symbol_orders_df,
        pair=pair,
        ltp=ltp,
        open_trade_count=config['open_trade_count'],
        step=config['step'],
        place_buy_order=place_buy_order,
        place_sell_order=place_sell_order,
    )


def run_multi_symbol_engine(orderDF, ltp_map, symbol_state):
    orders_by_symbol = split_orders_by_symbol(orderDF)

    for pair, config in SYMBOL_CONFIGS.items():
        symbol_orders = orders_by_symbol.get(pair)
        if symbol_orders is None or symbol_orders.empty:
            continue

        last_seen = symbol_state[pair]['last_updated_at']

        updated_orders = get_updated_orders(
            symbol_orders,
            last_seen
        )

        run_symbol_grid(
            pair=pair,
            config=config,
            symbol_orders_df=symbol_orders,
            updated_orders_df=updated_orders,
            ltp=ltp_map[pair],
        )

        # update watermark
        symbol_state[pair]['last_updated_at'] = symbol_orders['updated_at'].max()




# Main Loop
while True:
    orderDF = fetch_all_orders()       # paginated + cached
    ltp_map = fetch_all_ltps()          # {pair: ltp}

    run_multi_symbol_engine(
        orderDF=orderDF,
        ltp_map=ltp_map,
        symbol_state=symbol_state
    )

    time.sleep(2)


