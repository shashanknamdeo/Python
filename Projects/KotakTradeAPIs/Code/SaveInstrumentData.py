Username = 'SN28092002'
Passward = '_Sknam28'
Consumer_Key = '7Sivw6iASSCFNNgQia16uhbUQ98a'
Consumer_Secret = '3PzkUybzXXZOftP5Ap5iV5mJ2NYa'
Access_Token = 'b8171848-872e-3a12-a529-28bada211c56'
Access_Code = '5269'

from ks_api_client import ks_api
from datetime import datetime
import time

client = ks_api.KSTradeApi(access_token = Access_Token , userid = Username, \
                consumer_key = Consumer_Key, ip = "127.0.0.1", app_id = Consumer_Secret)

# Get session for user
client.login(password = Passward)

client.session_2fa(access_code = Access_Code)

def getLatestLTP():  
    try:
        # Get full quote details
        temp_quote_list = client.quote(instrument_token = 91623)
        quote_list = temp_quote_list['success']
        quote_dict = quote_list[0]
        ltp = float(quote_dict['ltp'])
        print(ltp)
    
    except Exception as e:
        print("Exception when calling QuoteApi->quote_details: %s\n" % e)

for i in range(0,6):
    time.sleep(1)
    ltp = getLatestLTP()
    curr_time = time.strftime("%H:%M:%S", time.localtime())


from pprint import pprint