# username = 'SN28092002'
# passward = '_Sknam28'
# consumer_key = '7Sivw6iASSCFNNgQia16uhbUQ98a'
# consumer_secret = '3PzkUybzXXZOftP5Ap5iV5mJ2NYa'
# access_token = 'b8171848-872e-3a12-a529-28bada211c56'
# access_code = '4487'

from ks_api_client import ks_api
from datetime import datetime
from datetime import date
import pandas as pd
import time

keylist = ['time','ltp','open_price','closing_price','high_price','low_price','average_trade_price','last_trade_qty','OI','display_segment','display_fno_eq']
keylist1 = ['ltp','open_price','closing_price','high_price','low_price','average_trade_price','last_trade_qty','OI','display_segment','display_fno_eq']


filename = "test.csv"

def askAccessCode():
    acess_code = str(input("Enter Access Code :"))
    return acess_code

def creatingClientSession():
    client = ks_api.KSTradeApi()
    # Get session for user
    client.login()
    session_2fa = client.session_2fa(access_code = askAccessCode())
    print("Session Created")
    # pprint(session_2fa)


def getLatestquote():  
    try:
        filename1 = ".csv"
        now = datetime.now()
        # Get full quote detail
        _dict = client.quote(instrument_token = 91623)['success'][0]
        # filename = _dict['stk_name'] + now.strftime("%d%m%Y") + filename1
        # data = pd.DataFrame(_dict, index=[0])
        valuelist = []
        valuelist.append(now.strftime("%d-%m-%Y %H:%M:%S"))
        for keys in keylist1:
            valuelist.append(_dict[keys])
        #
        # print(valuelist)
        return valuelist 
    #
    except Exception as e:
        print("Exception when calling QuoteApi->quote_details: %s\n" % e)

def main():
    creatingClientSession()
    df = pd.DataFrame(columns = keylist)
    while time.strftime("%H%M%S") <= '230000':
        quotelist = getLatestquote()
        df.loc[len(df.index)] = quotelist
        time.sleep(5)
        print(1)
    #
    df.to_csv(filename, header=True, index=False)

main()




# -------------------------------------------------------------------------------------------------

# import inspect
# inspect.getsourcelines((client.positions))

# client.positions(position_type = 'TODAYS')
# client.positions(position_type = 'OPEN')
# client.positions(position_type = 'STOCKS')