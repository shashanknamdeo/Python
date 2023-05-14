Username = 'SN28092002'
Passward = '_Sknam28'
Consumer_Key = '7Sivw6iASSCFNNgQia16uhbUQ98a'
Consumer_Secret = '3PzkUybzXXZOftP5Ap5iV5mJ2NYa'
Access_Token = 'b8171848-872e-3a12-a529-28bada211c56'


from ks_api_client import ks_api
from pprint import pprint
import pandas as pd


# Defining the host is optional and defaults to https://tradeapi.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
client = ks_api.KSTradeApi(access_token = Access_Token , userid = Username, consumer_key = Consumer_Key, ip = "127.0.0.1", app_id = Consumer_Secret)

# Get session for user
client.login(password = '_Sknam28')

#Generated session token
client.session_2fa(access_code = '5269')





# fetch instrument data

from ks_api_client import ks_api

client = ks_api.KSTradeApi(access_token = Access_Token , userid = Username, \
                consumer_key = Consumer_Key, ip = "127.0.0.1", app_id = Consumer_Secret)

# Get session for user
client.login(password = '_Sknam28')

client.session_2fa(access_code = '5269')



#First initialize session and generate session token

try:
    # Get full quote details
    client.quote(instrument_token = 91623)
    
    # Get quote details by quote_type
    # client.quote(instrument_token = 91623, quote_type = "LTP")
except Exception as e:
    print("Exception when calling QuoteApi->quote_details: %s\n" % e)



