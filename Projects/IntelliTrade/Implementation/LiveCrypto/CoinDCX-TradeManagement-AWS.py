"""
API: https://docs.coindcx.com/?python#futures-end-points

"""
import os
import sys

import uuid
import math
import json
import time
import hmac
import base64
import hashlib
import requests
import threading

import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint
from tabulate import tabulate
from datetime import datetime
from datetime import timezone

from decimal import Decimal
from decimal import ROUND_DOWN
from decimal import ROUND_HALF_UP

import boto3
from io import StringIO
from botocore.exceptions import ClientError

# --------------------------------------------------------------------------------------------------

def printTabulateDataFrame(dataframe, reset_index=False, drop_index_column=True, is_return=False, is_print=True):
    if reset_index:
        dataframe = dataframe.reset_index()
        if drop_index_column:
            dataframe = dataframe.drop(columns=['index'])
    # 
    # print(tabulate(dataframe, headers='keys', tablefmt='psql', floatfmt='.1f'))
    print(tabulate(dataframe, headers='keys', tablefmt='psql')) if is_print else None
    return tabulate(dataframe, headers='keys', tablefmt='psql') if is_return else None

# --------------------------------------------------------------------------------------------------
# AWS-Logging

import logging

def setup_logger():
    """
    AWS already has a log handler set up, so overriding the existing handlers.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # IMPORTANT: iterate over a copy
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    handler = logging.StreamHandler()
    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s"
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False  # avoid double logging

    return logger

logger = setup_logger()

# --------------------------------------------------------------------------------------------------
# config

global orderDF
global ledgerDF
global positionDF

global USDT_INR_RATE

USDT_INR_RATE = 96.0

SYMBOL_CONFIG = {
    "B-ETH_USDT": {
        "enabled": True,
        "open_trade_count"    : 1,
        "quantity"            : 0.007,
        "notional_value"      : 2304,
        "buy_step_price_diff" : 150,
        "sell_step_price_diff": 150,
        'quantity_tick_size'  : 0.001,
        'max_buy_price'       : 3000
    },
    "B-SOL_USDT": {
        "enabled": True,
        "open_trade_count"    : 4,
        "quantity"            : 0.05,
        "notional_value"      : 576,
        "buy_step_price_diff" : 3,
        "sell_step_price_diff": 3,
        'quantity_tick_size'  : 0.01,
        'max_buy_price'       : 140
    },
    "B-XRP_USDT": {
        "enabled": True,
        "open_trade_count"    : 4,
        "quantity"            : 3,
        "notional_value"      : 576,
        "buy_step_price_diff" : 0.04,
        "sell_step_price_diff": 0.04,
        'quantity_tick_size'  : 0.1,
        'max_buy_price'       : 2.20
    }
}

MAX_RETRIES = 3
BASE_BACKOFF = 0.5       # seconds
RATE_LIMIT_DELAY = 0.5  # seconds between requests

columns_order_list = ['pair', 'side', 'price', 'total_quantity', 'status', 'id', 'client_order_id', 'order_type', 'created_at', 'updated_at']
columns_position_list = ['pair', 'active_pos', 'inactive_pos_buy', 'inactive_pos_sell', 'liquidation_price', 'leverage']

# --------------------------------------------------------------------------------------------------
# Utils

def generate_timestamp():
    timestamp = int(round(time.time() * 1000))
    return timestamp


def fetch_api_response(url, body):
    """
    Method to fetch API-response and convert it into json and dataframe
    """
    headers, json_body = generate_headers_and_body(body)
    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    return data


def safe_post(url, headers, body):
    """
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(url, data=body, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        # 
        except Exception as e:
            if attempt == MAX_RETRIES:
                raise
            time.sleep(BASE_BACKOFF * (2 ** (attempt - 1)))


def epoch_to_datetime(series):
    """
    Safely converts timestamps to pandas datetime.
    Handles:
    - epoch milliseconds
    - epoch seconds
    - ISO strings
    """
    if pd.api.types.is_numeric_dtype(series):
        # Heuristic: large numbers → milliseconds
        if series.max() > 1e12:
            return pd.to_datetime(series, unit='ms', errors='coerce')
        else:
            return pd.to_datetime(series, unit='s', errors='coerce')
    else:
        return pd.to_datetime(series, errors='coerce')


def round_to_tick(value, tick):
    value = Decimal(str(value))
    tick = Decimal(str(tick))
    return (value / tick).to_integral_value(rounding=ROUND_HALF_UP) * tick


def response_api_check(response):
    """
    """
    # 1. HTTP-level failure
    if not response.ok:
        logger.error('HTTP: {} : {}'.format(response.status_code, response.text))
        raise RuntimeError(
            f"HTTP {response.status_code}: {response.text}"
        )
    # 
    # 2. JSON parse check
    try:
        data = response.json()
    except ValueError as e:
        logger.error('Invalid JSON response | error: {}'.format(e))
        raise RuntimeError("Invalid JSON response")
    # 
    # 3. API-level failure (ONLY if dict)
    if isinstance(data, dict):
        if data.get("success") is False:
            logger.error('API error')
            raise RuntimeError(f"API error: {data}")
    # 
    # logger.info('response: success')
    return data


def build_client_order_id(buy_client_order_id=None) -> str:
    """
    client_order_id must be unique all the time, even not equal to deleted 
    orders.
    max(len(client_order_id)) <=36
    pipe(|) and other special character cannot be used as a seperator. 
    only underscore(_) and hypen(-) are allowed.
    
    build_client_order_id(symbol='B-XRP_USDT', side='buy', price=1.75)
    
    for a new buy orders, input client_order_id=None, this a new is created.
    for an existing buy, to create a sell, provide client_order_id
    """
    if not buy_client_order_id:
        return f'ALGO-{uuid.uuid4().hex[:12]}-B-{uuid.uuid4().hex[:12]}'
    else:
        return buy_client_order_id[:17]+f'-S-{uuid.uuid4().hex[:12]}'


def calculate_min_quantity(price, notional_value, usdt_inr_rate, quantity_tick_size):
    """
    """
    def precision_from_tick(tick_size):
        return abs(Decimal(str(tick_size)).as_tuple().exponent)
    # 
    notional = Decimal(str(notional_value))
    price = Decimal(str(price))
    rate = Decimal(str(usdt_inr_rate))
    tick = Decimal(str(quantity_tick_size))
    # 
    raw_qty = notional / (price * rate)
    min_qty = math.ceil(raw_qty / tick) * tick
    precision = precision_from_tick(tick)
    min_qty = min_qty.quantize(tick, rounding=ROUND_DOWN)
    # 
    return float(min_qty)


def select_columns(data: dict, columns: list):
    return {k: data[k] for k in columns if k in data}

# --------------------------------------------------------------------------------------------------

def display_orderDF():
    logger.info('\n\norderDF :->')
    for pair, df_pair in orderDF.groupby("pair"):
        sorted_df = df_pair[columns_order_list].sort_values(by=['pair', 'side', 'price'], ascending=[True, False, False])
        logger.info('OrderDF | symbol: {}:->\n {}'.format(pair, printTabulateDataFrame(sorted_df, is_print=False, is_return=True)))


def display_ledgerDF():
    logger.info('\n\nledgerDF :->')
    for pair, df_pair in ledgerDF.groupby("pair"):
        sorted_df = df_pair[columns_order_list].sort_values(by=['pair', 'side', 'price'], ascending=[True, False, False])
        logger.info('ledgerDF | symbol: {}:->\n {}'.format(pair, printTabulateDataFrame(sorted_df, is_print=False, is_return=True)))


def display_positionDF():
    logger.info('\n\npositionDF :->\n {}'.format(printTabulateDataFrame(positionDF[columns_position_list], is_print=False, is_return=True)))


def get_symbol_info(symbol):
    """
    """
    url = 'https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair=&margin_currency_short_name=INR'.format(symbol)
    response = requests.get(url)
    data = response.json()
    pprint(data)


def update_positionDF():
    """
    """
    global positionDF
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/positions"
    # 
    body = {
        'timestamp':generate_timestamp(),
        'page': "1",
        'size': "10",
        'margin_currency_short_name': ['INR']
        }
    headers, json_body = generate_headers_and_body(body)
    response = requests.post(url, data = json_body, headers = headers)
    positionDF = pd.DataFrame(response_api_check(response))
    positionDF = positionDF[positionDF['active_pos'] > 0]
    logger.info('update -> positionDF')


def get_symbol_leverage(symbol):
    """
    """
    # update_positionDF()
    rows = positionDF[positionDF.pair==symbol]
    if rows.empty:
        logger.error('No leverage found for {}'.format(symbol))
        raise RuntimeError(f'No leverage found for {symbol}')
    # 
    leverage = rows.leverage.iloc[0]
    logger.info('symbol: {} | leverage: {}'.format(symbol, leverage))
    return leverage


def total_open_exposure():
    """
    """
    return (ledgerDF[ledgerDF.status=='initial'].total_quantity*ledgerDF.price*USDT_INR_RATE).sum()

# --------------------------------------------------------------------------------------------------
# Exchange-Methods

def fetch_futures_ltp(pair: str) -> float:
    """
    https://docs.coindcx.com/?python#get-current-prices-rt

    ls: last traded price, used for charts, display
    mp: mark price, used for PnL and liquadation

    fetch_futures_ltp(pair='B-ETH_USDT')
    fetch_futures_ltp(pair='B-SOL_USDT')
    fetch_futures_ltp(pair='B-XRP_USDT')
    """
    url_futures_price = "https://public.coindcx.com/market_data/v3/current_prices/futures/rt"
    response = requests.get(url_futures_price)
    data = response.json()
    return data['prices'][pair]['ls']


def symbols_ltp():
    for symbol in SYMBOL_CONFIG.keys():
        ltp = fetch_futures_ltp(symbol)
        logger.info('symbol: {} | ltp: {}'.format(symbol, ltp))


def update_orderDF():
    """
    """
    global orderDF
    time.sleep(2)
    # 
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders"
    # 
    status = ('open,filled,partially_filled,partially_cancelled,cancelled,rejected,untriggered')
    side = 'buy,sell'
    page_size = 200
    currency = 'INR'
    # 
    all_orders = []
    # 
    page = 1
    while True:
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
        page = page + 1
        time.sleep(RATE_LIMIT_DELAY)
    # 
    orderDF = pd.DataFrame(all_orders)
    orderDF = orderDF[(orderDF['client_order_id'].str.startswith('ALGO', na=False)) & (orderDF['status'].str.upper()!= 'CANCELLED')]
    # orderDF = orderDF.sort_values(by=['pair', 'side', 'price'], ascending=[True, False, False]).reset_index(drop=True)
    logger.info('update -> orderDF')


def create_order(symbol, side, order_type, price, quantity, client_order_id=None):
    """
    placeOrder(symbol='B-XRP_USDT', side='buy', order_type='limit_order', price=1.75, quantity=3.6)
    placeOrder(symbol='B-XRP_USDT', side='sell', order_type='limit_order', price=2.00, quantity=3.5)
    """
    url_create_order = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders/create"
    # 
    body = {
        'timestamp':generate_timestamp(),
        'order': {
            'pair'          : symbol,
            'side'          : side,
            'order_type'    : order_type,
            'price'         : str(price),
            'stop_price'    : str(price),
            'total_quantity': quantity,
            'leverage'      : get_symbol_leverage(symbol=symbol),
            'notification'  : 'no_notification',
            'time_in_force' : 'good_till_cancel',
            'hidden'        : False,
            'post_only'     : False,
            'margin_currency_short_name': 'INR',
            'client_order_id': build_client_order_id(client_order_id)
            }
        }
    # 
    time.sleep(1)
    headers, json_body = generate_headers_and_body(body)
    response = requests.post(url_create_order, data = json_body, headers = headers)
    return response_api_check(response)


def cancel_order(order_id):
    """
    """
    url_cancel_order = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders/cancel"
    body = {
        'timestamp': generate_timestamp(),
        'id'       : order_id
        }
    # 
    time.sleep(1)
    headers, json_body = generate_headers_and_body(body)
    response = requests.post(url_cancel_order, data = json_body, headers = headers)
    return response_api_check(response)


# --------------------------------------------------------------------------------------------------

def reconcile_ledger_with_exchange():
    """
    """
    logger.info('reconciliation -> started')
    FINAL_EXCHANGE_STATES = {
        'cancelled',
        'rejected',
        'partially_cancelled'
    }
    # 
    ledgerDF_open = ledgerDF[ledgerDF['status']=='initial'].copy()
    # 
    exchange_status_df = (orderDF[['client_order_id', 'status']].drop_duplicates().set_index('client_order_id'))
    # 
    for idx, row in ledgerDF_open.iterrows():
        client_order_id = row['client_order_id']
        # 
        if client_order_id not in exchange_status_df.index:
            logger.error('client_order_id: {} | Not found in exchange orders'.format(client_order_id))
            raise RuntimeError(f'client_order_id: {client_order_id} not found in exchange orders')
        # 
        exchange_status = exchange_status_df.loc[client_order_id, 'status']
        # 
        if exchange_status == 'filled':
            ledgerDF.at[idx, 'status'] = 'filled'
            logger.info('client_order_id: {} | status: initial -> filled'.format(client_order_id))
        elif exchange_status in FINAL_EXCHANGE_STATES:
            ledgerDF.at[idx, 'status'] = 'dead'
            logger.info('client_order_id: {} | status: initial -> dead'.format(client_order_id))
    # 
    logger.info('reconciliation -> completed')


def advance_filled_orders():
    """
    Move state machine forward:
    buy filled → place sell
    sell filled → place buy
    """
    logger.info('advance_fill -> started')
    global ledgerDF
    # 
    # BUY → SELL
    buys = ledgerDF[(ledgerDF.side == 'buy') & (ledgerDF.status == 'filled')]
    for idx, row in buys.iterrows():
        logger.info('buy filled client_order_id: {}'.format(row['client_order_id']))
        initiate_sell_order(row)
        ledgerDF.loc[idx, 'status'] = 'complete'
        save_ledger_to_disk_aws()
    # 
    # SELL → BUY
    sells = ledgerDF[(ledgerDF.side == 'sell') & (ledgerDF.status == 'filled')]
    for idx, row in sells.iterrows():
        logger.info('sell filled client_order_id: {}'.format(row['client_order_id']))
        initiate_buy_order(row)
        ledgerDF.loc[idx, 'status'] = 'complete'
        save_ledger_to_disk_aws()
    # 
    logger.info('advance_fill -> completed')


def initiate_sell_order(row):
    """
    When a buy order gets filled need to initiate its corresponding sell order and update ledger.
    """
    global ledgerDF
    # 
    symbol = row['pair']
    quantity = row['total_quantity']
    price = float(Decimal(str(row['price'])) + Decimal(str(SYMBOL_CONFIG[row['pair']]['sell_step_price_diff'])))
    client_order_id = row['client_order_id']
    # 
    logger.info('initiate sell | symbol: {} | side: {} | price: {} | quantity: {} |'.format(symbol, 'sell', price, quantity))
    response = create_order(symbol=symbol, side='sell', quantity=quantity, order_type='limit_order', price=price, client_order_id=client_order_id)
    logger.info(response)
    response_dict = select_columns(data=response[0], columns=columns_order_list)
    ledgerDF = pd.concat([ledgerDF, pd.DataFrame([response_dict])], ignore_index=True)
    save_ledger_to_disk_aws()
    logger.info('initiate  sell | success')


def initiate_buy_order(row):
    """
    When a sell order gets filled need to initiage its corresponding buy order, 
    but the quantity for the new order needs to be derived as per notional value
    so as to, we can adjust new buy quantities.
    """
    global ledgerDF
    # 
    symbol = row['pair']
    price = float(Decimal(str(row['price'])) - Decimal(str(SYMBOL_CONFIG[row['pair']]['buy_step_price_diff'])))
    # 
    symbol_dict = SYMBOL_CONFIG[symbol]
    quantity = calculate_min_quantity(price=price, notional_value=symbol_dict['notional_value'], usdt_inr_rate=USDT_INR_RATE, quantity_tick_size=symbol_dict['quantity_tick_size'])
    # 
    logger.info('initiate buy | symbol: {} | side: {} | price: {} | quantity: {} |'.format(symbol, 'buy', price, quantity))
    response = create_order(symbol=symbol, side='buy', quantity=quantity, order_type='limit_order', price=price)
    logger.info(response)
    response_dict = select_columns(data=response[0], columns=columns_order_list)
    ledgerDF = pd.concat([ledgerDF, pd.DataFrame([response_dict])], ignore_index=True)
    save_ledger_to_disk_aws()
    logger.info('initiate buy | success')


def find_missing_buy_grid_price_list(symbol):
    """
    """
    ltp = Decimal(str(fetch_futures_ltp(symbol)))
    open_trade_count = SYMBOL_CONFIG[symbol]['open_trade_count']
    buy_step_price_diff = Decimal(str(SYMBOL_CONFIG[symbol]['buy_step_price_diff']))
    # 
    base_price = math.floor(Decimal(str(ltp))/Decimal(str(buy_step_price_diff)))*Decimal(str(buy_step_price_diff))
    target_price_list = [base_price - i*buy_step_price_diff for i in range(0, open_trade_count)]
    # 
    existing_price_list = [Decimal(str(price)) for price in set(orderDF[(orderDF['pair']==symbol) & (orderDF['status']=='open')].price)]
    missing_price_list = [float(price) for price in target_price_list if price not in existing_price_list]
    # 
    return missing_price_list


def check_open_sell(symbol, buy_price):
    """
    Methood to check if no open sell order is present for a buy price?
    Returns:
        - True if not empty (ie sell exists)
        - False if empty (no sell side exists)
    Q. What if the sell order is present on the exchange but not on ledger? 
    That's why checking on both orderDF and ledgerDF.
    """
    sell_price = float(Decimal(str(buy_price)) + Decimal(str(SYMBOL_CONFIG[symbol]['sell_step_price_diff'])))
    orderDF_sell = orderDF[(orderDF['pair']==symbol) & (orderDF['side']=='sell') & (orderDF['price']==sell_price) & (orderDF['status']=='open')]
    ledgerDF_sell = ledgerDF[(ledgerDF['pair']==symbol) & (ledgerDF['side']=='sell') & (ledgerDF['price']==sell_price) & (ledgerDF['status']=='initial')]
    # 
    if not ledgerDF_sell.empty or not orderDF_sell.empty:
        return True
    else:
        return False


def place_missing_price_order(symbol):
    """
    """
    global orderDF
    global ledgerDF
    # 
    missing_price_list = find_missing_buy_grid_price_list(symbol)
    logger.info('symbol: {} | missing_price_list: {}'.format(symbol, missing_price_list))
    # 
    symbol_dict = SYMBOL_CONFIG[symbol]
    max_buy_price = SYMBOL_CONFIG[symbol]['max_buy_price']
    for price in missing_price_list:
        if not check_open_sell(symbol=symbol, buy_price=price) and price < max_buy_price:
            quantity = calculate_min_quantity(price=price, notional_value=symbol_dict['notional_value'], usdt_inr_rate=USDT_INR_RATE, quantity_tick_size=symbol_dict['quantity_tick_size'])
            logger.info('order | symbol: {} | side: {} | price: {} | quantity: {} |'.format(symbol, 'buy', price, quantity))
            response = create_order(symbol=symbol, side='buy', order_type='limit_order', price=price, quantity=quantity)
            logger.info(response)
            response_dict = select_columns(data=response[0], columns=columns_order_list)
            ledgerDF = pd.concat([ledgerDF, pd.DataFrame([response_dict])], ignore_index=True)
            logger.info('initiate buy | success')


def rebuild_grid():
    """
    Ensure grid invariants:
    - N buy orders per symbol
    - No duplicates
    - Respect max price
    """
    logger.info('rebuild_grid -> started')
    for symbol, symbol_dict in SYMBOL_CONFIG.items():
        if not symbol_dict['enabled']:
            logger.info('Exiting symbol: {} | enabled: {} | '.format(symbol, symbol_dict['enabled']))
            continue
        # 
        place_missing_price_order(symbol)
    logger.info('rebuild_grid -> completed')

# --------------------------------------------------------------------------------------------------

def run_engine():
    logger.info('\n\nENGINE START '+'='*80+'\n')
    # 
    # ─────────────────────────────────────────
    # PHASE 1: Load state
    # ─────────────────────────────────────────
    load_ledger_from_disk_aws()
    # 
    # ─────────────────────────────────────────
    # PHASE 2: Sync exchange truth
    # ─────────────────────────────────────────
    update_positionDF()
    update_orderDF()
    symbols_ltp()
    # 
    # ─────────────────────────────────────────
    # PHASE 3: Reconcile ledger
    # ─────────────────────────────────────────
    reconcile_ledger_with_exchange()
    # 
    # ─────────────────────────────────────────
    # PHASE 4: Advance state machines
    # ─────────────────────────────────────────
    advance_filled_orders()
    # 
    # ─────────────────────────────────────────
    # PHASE 5: Rebuild grid
    # ─────────────────────────────────────────
    update_orderDF()   # fetch orders created in phase 4
    rebuild_grid()
    # 
    # ─────────────────────────────────────────
    # PHASE 6: Persist state
    # ─────────────────────────────────────────
    save_ledger_to_disk_aws()
    # 
    # ─────────────────────────────────────────
    # PHASE 7: Statistics
    # ─────────────────────────────────────────
    update_orderDF()
    update_positionDF()
    # 
    display_orderDF()
    display_ledgerDF()
    display_positionDF()
    # 
    logger.info('\n\nENGINE END '+'='*80+'\n\n')

# --------------------------------------------------------------------------------------------------
# AWS-Functions


def load_ledger_from_disk_aws():
    """
    """
    global ledgerDF
    bucket_name = 'amzn-s3-bucket-coindcx'
    file_key = 'data/LedgerDF.csv'
    # 
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    csv_content = obj['Body'].read().decode('utf-8')
    ledgerDF = pd.read_csv(StringIO(csv_content))
    logger.info('load -> ledgerDF')


def save_ledger_to_disk_aws():
    """
    """
    global ledgerDF
    bucket_name = 'amzn-s3-bucket-coindcx'
    file_key = 'data/LedgerDF.csv'
    csv_buffer = StringIO()
    ledgerDF.to_csv(csv_buffer, index=False)
    # 
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=csv_buffer.getvalue())
    logger.info('save -> ledgerDF')

# -------------------------------------------------------------------------------------------------

