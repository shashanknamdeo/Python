username = 'SN28092002'
passward = '_Sknam28'
consumer_key = '7Sivw6iASSCFNNgQia16uhbUQ98a'
consumer_secret = '3PzkUybzXXZOftP5Ap5iV5mJ2NYa'
access_token = 'b8171848-872e-3a12-a529-28bada211c56'
access_code = '5269'

from ks_api_client import ks_api
from datetime import datetime
from pprint import pprint
import pandas as pd
import time

client = ks_api.KSTradeApi(access_token = access_token , userid = username, \
                consumer_key = consumer_key, ip = "127.0.0.1", app_id = consumer_secret)

# Get session for user
client.login(password = passward)

session_2fa = client.session_2fa(access_code = access_code)
pprint(session_2fa)

# -------------------------------------------------------------------------------------------------

import inspect
inspect.getsourcelines((client.positions))

client.positions(position_type = 'TODAYS')
client.positions(position_type = 'OPEN')
client.positions(position_type = 'STOCKS')



_dict = client.quote(instrument_token = 91623)['success'][0]
pd.DataFrame(_dict, index=[0])


def getLatestLTP():  
    try:
        # Get full quote detail
        ltp = float(quote_dict['ltp'])
        print(ltp)
    
    except Exception as e:
        print("Exception when calling QuoteApi->quote_details: %s\n" % e)

for i in range(0,6):
    time.sleep(1)
    ltp = getLatestLTP()
    curr_time = time.strftime("%H:%M:%S", time.localtime())


from pprint import pprint