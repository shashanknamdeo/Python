
from ks_api_client import ks_api
from datetime import datetime
from datetime import date
import pandas as pd
import time
import sys
import os

Kotak_Data_Dir = r'D:\ShashankPC\Material\Python\Projects\KotakTradeAPIs\Data'

Daily_Data_Dir_path = os.path.join(Kotak_Data_Dir, 'DailyData')
os.makedirs(Daily_Data_Dir_path, exist_ok=True)

instrument_name_list = ['ABSLLIQUID','ABSLAMC','BSLGOLDETF','MOMENTUM','NIFTYQLITY','BSLNIFTY','ABSLBANETF','HEALTHY','TECH','ABSLNN50ET','BSLSENETFG']
instrument_token_list = []

keylist = ['time','ltp','open_price','closing_price','high_price','low_price','average_trade_price','last_trade_qty','OI','display_segment']
keylist1 = ['ltp','open_price','closing_price','high_price','low_price','average_trade_price','last_trade_qty','OI','display_segment']


def getInstrumentToken(verbose = 0):
    df = pd.read_csv(os.path.join(Kotak_Data_Dir, 'Tokens', 'EquityInstrumentTokens', 'EquityInstrumentTokensNSE.csv'))
    for instrument_name in instrument_name_list:
        instrument_token_list.append(df.loc[df['instrumentName'] == instrument_name, 'instrumentToken'].iloc[0])
    print("instrument_token_list updated") if verbose >=1 else None


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
        
def getFileName(instrument_name):
    now = datetime.now()
    # _dict = client.quote(instrument_token = token_no)['success'][0]
    filename = instrument_name + now.strftime("%d%m%Y") + '.csv'
    return filename


def checkFileInDir(file_name, verbose = 0):
    file_path = os.path.join(Kotak_Data_Dir, 'DailyData', file_name)
    # print(file_path)
    # print(os.path.isfile(file_path))
    if os.path.isfile(file_path) == False:
        # with open(os.path.join(Kotak_Data_Dir, 'DailyData', filename), mode) as f:
        with open(file_path, 'w') as f:
            f.write(getCSVLikeStringByList(_list = keylist) + '\n')
            pass
            print('File Created') if verbose >=1 else None
            #
    else :
        print('File Already Exist') if verbose >=1 else None


def askAccessCode():
    acess_code = str(input("Enter Access Code :"))
    return acess_code


def getLatestquote(token_no, verbose = 0):  
    try:
        now = datetime.now()
        print(now) if verbose >=1 else None
        # Get full quote detail
        _dict = client.quote(token_no)['success'][0]
        #
        value_string = ''
        value_string = value_string + now.strftime("%d-%m-%Y %H:%M:%S") + ','
        for key in keylist1:
            value_string = value_string + _dict[key] + ','
        #
        value_string = value_string[:-1]
        print(value_string) if verbose >=1 else None
        return value_string
    #
    except Exception as e:
        print("Exception when calling QuoteApi->quote_details: %s\n" % e)


def getCSVLikeStringByList(_list):
    string = ''
    for element in _list:
        string = string + element + ','
    #
    string = string[:-1]
    return string


# To create session
username, password, consumer_key, consumer_secret, access_token = getKiteConnectCredentials(Kotak_Data_Dir)
#
client = ks_api.KSTradeApi(access_token = access_token , userid = username, consumer_key = consumer_key, ip = "127.0.0.1", app_id = consumer_secret)
#
client.login(password = password)
#
client.session_2fa(access_code = askAccessCode())
print("Session Created")
#
#
# To save file name
file_name_list = []
for instrument_name in instrument_name_list:
    file_name_list.append(getFileName(instrument_name = instrument_name))
# print(file_name_list) if verbose >=1 else None
#
#
# To create file with header and with file name
for file_name in file_name_list:
    checkFileInDir(file_name = file_name)
print("All instrument files checked")
#
#
# To get token_no
getInstrumentToken()
print("Token list updated")
# print(instrument_token_list) if verbose >=1 else None
#
#
#
if len(instrument_name_list) == len(instrument_token_list) and len(instrument_name_list) == len(file_name_list):
    flag = ''
    while time.strftime("%H%M%S") <= '230000' and flag == '':
        for i in range(0,len(instrument_name_list)):
            # print(instrument_token_list[i]) if verbose >=1 else None
            value_string = getLatestquote(token_no = int(instrument_token_list[i]))
            with open(os.path.join(Kotak_Data_Dir, 'DailyData', file_name_list[i]), "a") as f:
                f.write(value_string + '\n')
                f.close()
        #
        # time.sleep(5)
        flag = str(input("enter desision :"))





# print(client.quote(60862)['success'][0])
# print(client.quote(10809)['success'][0])
# getLatestquote(10809)


# df = pd.DataFrame(columns = keylist)
# while time.strftime("%H%M%S") <= '230000':
#     quotelist = getLatestquote()
#     df.loc[len(df.index)] = quotelist
#     print(1)
#     time.sleep(5)
# #
# df.to_csv(getFileName(), header=True, index=False)


            


# -------------------------------------------------------------------------------------------------

# import inspect
# inspect.getsourcelines((client.positions))

# client.positions(position_type = 'TODAYS')
# client.positions(position_type = 'OPEN')
# client.positions(position_type = 'STOCKS')