
from ks_api_client import ks_api
from datetime import datetime
from datetime import date
import pandas as pd
import time
import sys
import os

Kotak_Data_Dir = r'D:\ShashankPC\Material\Python\Projects\KotakTradeAPIs\Data'

keylist = ['time','ltp','open_price','closing_price','high_price','low_price','average_trade_price','last_trade_qty','OI','display_segment','display_fno_eq']
keylist1 = ['ltp','open_price','closing_price','high_price','low_price','average_trade_price','last_trade_qty','OI','display_segment','display_fno_eq']


filename = "test.csv"

def getKiteConnectCredentials(Kotak_Data_Dir):
    """
    getKiteConnectCredentials(r'D:\ShashankPC\Material\Python\Projects\KotakTradeAPIs\Data')
    """
    with open(os.path.join(Kotak_Data_Dir, 'Security', 'KotakCredentials.txt'), 'r') as credentialsFile:
        credentialData = credentialsFile.readlines()
        username        = credentialData[0].split(':')[1].strip()
        password        = credentialData[1].split(':')[1].strip()
        consumer_key    = credentialData[2].split(':')[1].strip()
        consumer_secret = credentialData[3].split(':')[1].strip()
        access_token    = credentialData[4].split(':')[1].strip()
        return (username, password, consumer_key, consumer_secret, access_token)
        

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
        _dict = client.quote(instrument_token = 15448)['success'][0]
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

def getFileName():
    now = datetime.now()
    _dict = client.quote(instrument_token = 15448)['success'][0]
    filename = _dict['stk_name'] + now.strftime("%d%m%Y") + '.csv'
    return filename


username, password, consumer_key, consumer_secret, access_token = getKiteConnectCredentials(Kotak_Data_Dir)
#
client = ks_api.KSTradeApi(access_token = access_token , userid = username, consumer_key = consumer_key, ip = "127.0.0.1", app_id = consumer_secret)
#
client.login(password = password)
#
client.session_2fa(access_code = askAccessCode())
print("Session Created")
df = pd.DataFrame(columns = keylist)
while time.strftime("%H%M%S") <= '230000':
    quotelist = getLatestquote()
    df.loc[len(df.index)] = quotelist
    print(1)
    time.sleep(5)
#
df.to_csv(getFileName(), header=True, index=False)



def checkFileInDir():
    file_name = getFileName()
    Daily_Data_Dir_path = os.path.join(Kotak_Data_Dir, 'DailyData')
    file_path = os.path.join(Kotak_Data_Dir, 'DailyData', file_name)
    # print(file_path)
    os.makedirs(Daily_Data_Dir_path, exist_ok=True)
    # print(os.path.isfile(file_path))
    if os.path.isfile(file_path) == False:
        # with open(os.path.join(Kotak_Data_Dir, 'DailyData', filename), mode) as f:
        with open(file_path, 'w') as f:
            pass
            print('File Created')
            #
    else :
        print('File Already Exist')

            


# -------------------------------------------------------------------------------------------------

# import inspect
# inspect.getsourcelines((client.positions))

# client.positions(position_type = 'TODAYS')
# client.positions(position_type = 'OPEN')
# client.positions(position_type = 'STOCKS')