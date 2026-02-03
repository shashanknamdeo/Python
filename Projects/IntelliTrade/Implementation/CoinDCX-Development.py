def update_ledger_with_buy_filled_orders():
    """
    Method to check wether any of the buy order has been filled or not.
    It takes open(initial) order from the ledgerDF and compare the status with 
    orderDF's staus.
    If buy order is filled: updated ledger status and initiate its sell order
    """
    ledgerDF_open = ledgerDF[(ledgerDF['side']=='buy') & (ledgerDF['status']=='initial')].copy()
    opened_buy_order_count  = ledgerDF_open.shape[0]
    logger.debug('LedgerDF -> opened_buy_order_count: {}'.format(opened_buy_order_count))
    # 
    for _, row in ledgerDF_open.iterrows():
        logger.debug('client_order_id: {} | status: {}'.format(row['client_order_id'], row['status']))
        if orderDF[orderDF.client_order_id==row['client_order_id']].status.values[0] == 'filled':
            condition = (ledgerDF['client_order_id'] == row['client_order_id'])
            ledgerDF.loc[condition, 'status'] = 'filled'
            logger.debug('Update | status: initial -> filled | client_order_id: {}'.format(row['client_order_id']))
            # 
            initiate_sell_order(row)


def update_ledger_with_sell_filled_orders():
    """
    Method to check wether any of the buy order has been filled or not.
    """
    ledgerDF_open = ledgerDF[(ledgerDF['side']=='sell') & (ledgerDF['status']=='initial')].copy()
    opened_sell_order_count  = ledgerDF_open.shape[0]
    logger.debug('LedgerDF -> opened_sell_order_count: {}'.format(opened_sell_order_count))
    # 
    for _, row in ledgerDF_open.iterrows():
        logger.debug('client_order_id: {} | status: {}'.format(row['client_order_id'], row['status']))
        if orderDF[orderDF.client_order_id==row['client_order_id']].status.values[0] == 'filled':
            condition = (ledgerDF['client_order_id'] == row['client_order_id'])
            ledgerDF.loc[condition, 'status'] = 'filled'
            logger.debug('Update | status: initial -> filled | client_order_id: {}'.format(row['client_order_id']))
            initiate_buy_order(row)


def showOpenOrders():
    """
    """
    list_order_dict = createListOrderDict(status='open', side='sell')
    data, orderDF = fetch_api_response(url=url_orders_futures, body=list_order_dict)
    orderDF = orderDF[['pair', 'price', 'total_quantity', 'side', 'status', 'order_type', 'remaining_quantity', 'leverage', 'maker_fee', 'taker_fee']]
    printTabulateDataFrame(orderDF.sort_values(by=['pair', 'price'], ascending=[True, False], ignore_index=True))
    # 
    list_order_dict = createListOrderDict(status='open', side='buy')
    data, orderDF = fetch_api_response(url=url_orders_futures, body=list_order_dict)
    orderDF = orderDF[['pair', 'price', 'total_quantity', 'side', 'status', 'order_type', 'remaining_quantity', 'leverage', 'id']]
    printTabulateDataFrame(orderDF.sort_values(by=['pair', 'price'], ascending=[True, False], ignore_index=True))

# --------------------------------------------------------------------------------------------------

import json
import time
import hmac
import base64
import hashlib
import requests

import pandas as pd
from pprint import pprint

import code
code.interact(local=globals())

# --------------------------------------------------------------------------------------------------

timestamp = int(round(time.time() * 1000))


url_orders_futures = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders"

# --------------------------------------------------------------------------------------------------

# List-Positions
# https://docs.coindcx.com/?python#list-positions

body = {
        "timestamp":timeStamp , # EPOCH timestamp in seconds
        "page": "1", #no. of pages needed
        "size": "10",
        "margin_currency_short_name": ["INR"] #["USDT"]
        }


json_body = json.dumps(body, separators = (',', ':'))

url = "https://api.coindcx.com/exchange/v1/derivatives/futures/positions"


response = requests.post(url, data = json_body, headers = headers)
data = response.json()
print(data)

ordersDF = pd.DataFrame(data)





orderDF = fetch_orders()

ltp = fetch_futures_ltp('B-XRP_USDT')
missing_grids_prices = maintain_buy_grid(orderDF, pair='B-XRP_USDT', ltp=fetch_futures_ltp('B-XRP_USDT'), open_trade_count=4, step_price_diff=0.04)['missing_grids_prices']

response_list = []
for missing_price in missing_grids_prices:
    response = placeOrder(symbol='B-XRP_USDT', side='buy', order_type='limit_order', price=missing_price, quantity=4)
    response_list.append(response)

ltp = fetch_futures_ltp('B-SOL_USDT')
missing_grids_prices = maintain_buy_grid(orderDF, pair='B-SOL_USDT', ltp=fetch_futures_ltp('B-SOL_USDT'), open_trade_count=2, step_price_diff=3)['missing_grids_prices']

response_list = []
for missing_price in missing_grids_prices:
    response = placeOrder(symbol='B-SOL_USDT', side='buy', order_type='limit_order', price=missing_price, quantity=0.05)
    response_list.append(response)




# ------------------------------------------------------------------------------
output: create_order
{'avg_price': 0.0,
 'cancelled_quantity': 0.0,
 'client_order_id': 'algo', -> This was passed explicitly by us.
 'created_at': 1769365926132,
 'display_message': None,
 'fee_amount': 0.0,
 'group_id': None,
 'group_status': None,
 'id': '964b6d52-2e85-4bb9-9632-27d8658ad5b6',
 'ideal_margin': 3.003717,
 'leverage': 2.1,
 'liquidation_fee': None,
 'maker_fee': 0.0236,
 'margin_currency_short_name': 'INR',
 'notification': 'no_notification',
 'order_category': None,
 'order_type': 'limit_order',
 'pair': 'B-XRP_USDT',
 'position_margin_type': 'isolated',
 'price': 1.8,
 'remaining_quantity': 3.5,
 'settlement_currency_conversion_price': 96.0,
 'side': 'buy',
 'stage': 'default',
 'status': 'initial',
 'stop_loss_price': None,
 'stop_price': 1.8,
 'stop_trigger_instruction': 'last_price',
 'take_profit_price': None,
 'taker_fee': 0.059,
 'total_quantity': 3.5,
 'updated_at': 1769365926132}



>>> pprint(data[0])
{'active_pos': 64.2,
 'avg_price': 2.02502476381836,
 'id': '009dcf70-c1c8-11f0-94fb-df014fe43fc2',
 'inactive_pos_buy': 13.8,
 'inactive_pos_sell': 19.9,
 'leverage': 2.1,
 'liquidation_price': 1.0711,
 'locked_margin': 61.89545636481742,
 'locked_order_margin': 11.66647478809525,
 'locked_user_margin': 61.98864829737504,
 'maintenance_margin': 0.61641887763,
 'margin_currency_short_name': 'INR',
 'margin_type': 'isolated',
 'mark_price': 1.92030803,
 'pair': 'B-XRP_USDT',
 'settlement_currency_avg_price': 96.0,
 'stop_loss_trigger': None,
 'take_profit_trigger': None,
 'updated_at': 1769107996641}





SELL_ORDER
>>> pprint(data[0])
{'avg_price': 0.0,
 'cancelled_quantity': 0.0,
 'client_order_id': None,
 'created_at': 1769107611647,
 'display_message': 'SOL limit sell order placed!',
 'fee_amount': 0.0,
 'group_id': None,
 'group_status': None,
 'id': 'b7d49e2b-38fe-4871-b2a5-b80388d5ab4e',
 'ideal_margin': 3.14675114285714,
 'leverage': 2.1,
 'liquidation_fee': None,
 'maker_fee': 0.0236,
 'margin_currency_short_name': 'INR',
 'notification': 'email_notification',
 'order_category': None,
 'order_type': 'limit_order',
 'pair': 'B-SOL_USDT',
 'position_margin_type': 'isolated',
 'price': 132.0,
 'remaining_quantity': 0.05,
 'settlement_currency_conversion_price': 96.0,
 'side': 'sell',
 'stage': 'default',
 'status': 'open',
 'stop_loss_price': None,
 'stop_price': 0.0,
 'stop_trigger_instruction': 'last_price',
 'take_profit_price': None,
 'taker_fee': 0.059,
 'total_quantity': 0.05,
 'updated_at': 1769107611762}

BUY_ORDER
>>> pprint(data[0])
{'avg_price': 0.0,
 'cancelled_quantity': 0.0,
 'client_order_id': None,
 'created_at': 1769021630008,
 'display_message': 'SOL limit buy order placed!',
 'fee_amount': 0.0,
 'group_id': None,
 'group_status': None,
 'id': 'c490fe49-1c19-473a-aac9-761cd8ec8a40',
 'ideal_margin': 3.003717,
 'leverage': 2.1,
 'liquidation_fee': None,
 'maker_fee': 0.0236,
 'margin_currency_short_name': 'INR',
 'notification': 'email_notification',
 'order_category': None,
 'order_type': 'limit_order',
 'pair': 'B-SOL_USDT',
 'position_margin_type': 'isolated',
 'price': 126.0,
 'remaining_quantity': 0.05,
 'settlement_currency_conversion_price': 96.0,
 'side': 'buy',
 'stage': 'default',
 'status': 'open',
 'stop_loss_price': None,
 'stop_price': 0.0,
 'stop_trigger_instruction': 'last_price',
 'take_profit_price': None,
 'taker_fee': 0.059,
 'total_quantity': 0.05,
 'updated_at': 1769105680545}


url = 'https://api.coindcx.com/exchange/v1/users/info'
url = 'https://api.coindcx.com/exchange/v1/orders/active_orders'
url = 'https://api.coindcx.com/exchange/v1/orders/active_orders_count'
url = "https://api.coindcx.com/exchange/v1/margin/fetch_orders"


timeStamp = int(round(time.time() * 1000))

json_body = json.dumps(body, separators = (',', ':'))

response = requests.post(url, data = json_body, headers = headers)
data = response.json()
print(data)


body = {
  "from_id": 352622,
  "limit": 50,
  "timestamp": timeStamp,
  "sort": "asc",
  "from_timestamp": 1514745000000, # replace this with your from timestamp filter
  "to_timestamp": 1514745000000, # replace this with your to timestamp filter
  "symbol": "BCHBTC" # replace this with your symbol filter
}


timeStamp = int(round(time.time() * 1000))
body = {
        "timestamp": timeStamp , # EPOCH timestamp in seconds
        "status": "open", # Comma separated statuses as open,filled,cancelled
        "side": "sell", # buy OR sell
        "page": "1", #// no.of pages needed
        "size": "10", #// no.of records needed
    "margin_currency_short_name": ["INR", "USDT"]
        }

json_body = json.dumps(body, separators = (',', ':'))

url = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders"

response = requests.post(url, data = json_body, headers = headers)
data = response.json()
print(data)

B-SOL_USDT

>>> pprint.pprint(data[0])
{'avg_price': 0.0,
 'cancelled_quantity': 0.0,
 'client_order_id': None,
 'created_at': 1763786523149,
 'display_message': 'SOL limit sell order placed!',
 'fee_amount': 0.0,
 'group_id': None,
 'group_status': None,
 'id': '60924104-791a-40a6-9e81-d00fc7d3f000',
 'ideal_margin': 3.39854234210526,
 'leverage': 1.9,
 'liquidation_fee': None,
 'maker_fee': 0.0236,
 'margin_currency_short_name': 'INR',
 'notification': 'email_notification',
 'order_category': None,
 'order_type': 'limit_order',
 'pair': 'B-SOL_USDT',
 'position_margin_type': 'isolated',
 'price': 129.0,
 'remaining_quantity': 0.05,
 'settlement_currency_conversion_price': 96.0,
 'side': 'sell',
 'stage': 'default',
 'status': 'open',
 'stop_loss_price': None,
 'stop_price': 0.0,
 'stop_trigger_instruction': 'last_price',
 'take_profit_price': None,
 'taker_fee': 0.059,
 'total_quantity': 0.05,
 'updated_at': 1763786523551}
>>>



-----------------
Working

import json
import boto3
import os
import urllib.request

S3_BUCKET = os.environ.get("S3_BUCKET")  # configure this in Lambda console

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # 1) call an external API (example: httpbin.org)
    try:
        with urllib.request.urlopen("https://httpbin.org/get") as resp:
            body = resp.read().decode("utf-8")
    except Exception as e:
        body = json.dumps({"error": str(e)})
    
    # 2) store response summary to S3
    summary = {
        "timestamp": context.aws_request_id if context else "no-context",
        "sample_response_len": len(body)
    }
    s3.put_object(Bucket=S3_BUCKET, Key=S3_KEY, Body=json.dumps(summary).encode("utf-8"))
    
    # 3) optionally read the file back (demo)
    obj = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    contents = obj['Body'].read().decode('utf-8')

    return {
        "statusCode": 200,
        "body": json.dumps({"s3_summary": json.loads(contents)})
    }


-------------------------

pair = "B-ETH_USDT"
url = f"https://public.coindcx.com/market_data/trade_history?pair={pair}&limit=1"

url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair=B-ETH_USDT&margin_currency_short_name=INR"
url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments?margin_currency_short_name[]=INR"
response = requests.get(url)
data = response.json()


url = "https://api.coindcx.com/exchange/v1/markets"
response = requests.get(url)
data = response.json()
print(data)


url = "https://api.coindcx.com/exchange/ticker"
response = requests.get(url)
data = response.json()
print(data)
data[0]
{'market': 'FIOINR', 'change_24_hour': '1.051', 'high': '1.01304', 'low': '1.0025', 'volume': '316.8747039', 'last_price': '1.0130400000', 'bid': '1.0197600000', 'ask': '1.0669000000', 'timestamp': 1769261137}
for item in data:
    if item['market']=='ETHUSDT':
    item
# Above shows the price of the spot market.


url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair=B-ETH_USDT"
response = requests.get(url)
data = response.json()
print(data)



time.strftime("%H:%M:%S", time.localtime(timesspamp))
datetime.fromtimestamp(1769287471937 / 1000).strftime("%Y/%m/%d %H:%M:%S")





[{'id': '1a8643cd-2851-4935-98a5-7747313fea79', 'client_order_id': None, 'pair': 'B-XRP_USDT', 'side': 'buy', 'status': 'initial', 'order_type': 'limit_order', 'stop_trigger_instruction': 'last_price', 'notification': 'no_notification', 'leverage': 2.1, 'maker_fee': 0.0236, 'taker_fee': 0.059, 'fee_amount': 0.0, 'price': 1.85, 'stop_price': 1.85, 'avg_price': 0.0, 'total_quantity': 4.0, 'remaining_quantity': 4.0, 'cancelled_quantity': 0.0, 'ideal_margin': 3.52817552380952, 'order_category': None, 'stage': 'default', 'group_id': None, 'liquidation_fee': None, 'position_margin_type': 'isolated', 'settlement_currency_conversion_price': 96.0, 'take_profit_price': None, 'stop_loss_price': None, 'margin_currency_short_name': 'INR', 'display_message': None, 'group_status': None, 'created_at': 1769287471501, 'updated_at': 1769287471501}]
[{'id': 'a5b550cf-37ac-4ff5-a47f-bc3d5abb214d', 'client_order_id': None, 'pair': 'B-XRP_USDT', 'side': 'buy', 'status': 'initial', 'order_type': 'limit_order', 'stop_trigger_instruction': 'last_price', 'notification': 'no_notification', 'leverage': 2.1, 'maker_fee': 0.0236, 'taker_fee': 0.059, 'fee_amount': 0.0, 'price': 1.75, 'stop_price': 1.75, 'avg_price': 0.0, 'total_quantity': 4.0, 'remaining_quantity': 4.0, 'cancelled_quantity': 0.0, 'ideal_margin': 3.33746333333333, 'order_category': None, 'stage': 'default', 'group_id': None, 'liquidation_fee': None, 'position_margin_type': 'isolated', 'settlement_currency_conversion_price': 96.0, 'take_profit_price': None, 'stop_loss_price': None, 'margin_currency_short_name': 'INR', 'display_message': None, 'group_status': None, 'created_at': 1769287471714, 'updated_at': 1769287471714}]
[{'id': '39a454f7-b802-4595-ba27-250c1b1256b4', 'client_order_id': None, 'pair': 'B-XRP_USDT', 'side': 'buy', 'status': 'initial', 'order_type': 'limit_order', 'stop_trigger_instruction': 'last_price', 'notification': 'no_notification', 'leverage': 2.1, 'maker_fee': 0.0236, 'taker_fee': 0.059, 'fee_amount': 0.0, 'price': 1.7, 'stop_price': 1.7, 'avg_price': 0.0, 'total_quantity': 4.0, 'remaining_quantity': 4.0, 'cancelled_quantity': 0.0, 'ideal_margin': 3.24210723809524, 'order_category': None, 'stage': 'default', 'group_id': None, 'liquidation_fee': None, 'position_margin_type': 'isolated', 'settlement_currency_conversion_price': 96.0, 'take_profit_price': None, 'stop_loss_price': None, 'margin_currency_short_name': 'INR', 'display_message': None, 'group_status': None, 'created_at': 1769287471937, 'updated_at': 1769287471937}]

# Placed order response
>>> pprint(x)
[{'avg_price': 0.0,
  'cancelled_quantity': 0.0,
  'client_order_id': None,
  'created_at': 1769287471501,
  'display_message': None,
  'fee_amount': 0.0,
  'group_id': None,
  'group_status': None,
  'id': '1a8643cd-2851-4935-98a5-7747313fea79',
  'ideal_margin': 3.52817552380952,
  'leverage': 2.1,
  'liquidation_fee': None,
  'maker_fee': 0.0236,
  'margin_currency_short_name': 'INR',
  'notification': 'no_notification',
  'order_category': None,
  'order_type': 'limit_order',
  'pair': 'B-XRP_USDT',
  'position_margin_type': 'isolated',
  'price': 1.85,
  'remaining_quantity': 4.0,
  'settlement_currency_conversion_price': 96.0,
  'side': 'buy',
  'stage': 'default',
  'status': 'initial',
  'stop_loss_price': None,
  'stop_price': 1.85,
  'stop_trigger_instruction': 'last_price',
  'take_profit_price': None,
  'taker_fee': 0.059,
  'total_quantity': 4.0,
  'updated_at': 1769287471501}]



I need Both (full grid bot)
BUY filled → place SELL above
Also refill BUY grid below to maintain count.
I don't need that into just a single function, better maked it multiple independent functions and production grade code.

My logic is keep tracking the buy open orders. If price fall below then:
a. Maintain buy grid using maintain_buy_grid function.
b. If a open order is already filled then place its sell side order.
c. If the sell order is filled then place its buy order again.

# Development

def checkUpdatedAtOrder(orderDF):
    """
    Function to check wether the orderDF & orders returned by API is sorted with updated_at or not.
    Observed that the orders list returnd is sort from newest to oldest updated_at.
    """
    # Ensure datetime columns are actually datetime and not strings
    orderDF['created_at'] = pd.to_datetime(orderDF['created_at'])
    orderDF['updated_at'] = pd.to_datetime(orderDF['updated_at'])
    # 
    # Check if DataFrame is sorted by updated_at (descending)
    is_updated_sorted = orderDF['updated_at'].is_monotonic_decreasing
    is_created_sorted = orderDF['created_at'].is_monotonic_decreasing
    print("Sorted by updated_at:", is_updated_sorted)
    print("Sorted by created_at:", is_created_sorted)
    # 
    # Stronger verification (detect actual sort key)
    updated_diff = orderDF['updated_at'].diff().dropna()
    created_diff = orderDF['created_at'].diff().dropna()
    print("updated_at mostly descending:", (updated_diff <= pd.Timedelta(0)).mean())
    print("created_at mostly descending:", (created_diff <= pd.Timedelta(0)).mean())


response = placeOrder(market='B-XRP_USDT', side='buy', order_type='limit_order', price=1.80, quantity=3.5)

