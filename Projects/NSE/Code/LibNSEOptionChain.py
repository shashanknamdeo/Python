# Libraries
import requests
import json
import math

# import KiteConnectSysPath
# from GlobalVariables import DROPBOX_TRADING_OPTION_CHAIN_DATA_DIR

DROPBOX_TRADING_OPTION_CHAIN_DATA_DIR = r'D:\Trading\OptionChainData'

# from LibSaveDataFrameToDisk import saveDataFrameToDisk
# from LibLoadDataFrameFromDisk import loadCSVFileFromDirectoryIntoDataFrame
# from LibFileNames import fetchAllFilesinDirectory
# from LibMatplotlibPlots import matplotlibPlot
# from LibMatplotlibPlots import matplotlibDualAxisPlot

def saveDataFrameToDisk(dataframe_to_save, directory_path, file_name=None, file_extension='csv', save_with_headers=True, save_with_index=False):
    """
    Generic method to save a pandas dataframe to disk.
    saveDataFrameToDisk(dataframe_to_save=optionChainDF, dir_path=dir_path, file_extension='csv')
    """
    
    import os
    import re
    import pandas as pd
    from datetime import datetime
    # 
    # Checking valid file extension
    file_extension_list = ['.csv']
    if re.search(r'\.[a-z]+', file_extension) is not None:
        pass
    else:
        file_extension = '.'+file_extension
    # 
    if file_extension in file_extension_list:
        pass
    else:
        raise Exception('Unsupported file_extension: {}'.format(file_extension))
    #
    file_time = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    file_path = os.path.join(directory_path, file_time+file_extension)
    try:
        pd.DataFrame(dataframe_to_save).to_csv(file_path, index=False)
    except Exception as e:
        raise Exception('Cannot Save DataFrame {}'.format(e))
    # 
    return True

def loadCSVFileFromDirectoryIntoDataFrame(file_path, load_with_headers=True):
    """
    Generic method to load a pandas dataframe to disk.
    loadDataFrameFromDisk(file_path=file_path)
    """
    import pandas as pd
    try:
        dataframe = pd.read_csv(file_path)
    except:
        raise Exception('Cannot Load DataFrame')
    # 
    return dataframe

def fetchAllFilesinDirectory(directory_path, full_path=True):
    """
    """
    # directory_path=r'D:\NotebookShareAsus\Material\Spark\SparkInternals'
    import os
    dir_items = os.listdir(path=directory_path)
    # 
    file_list = []
    for item in dir_items:
        if os.path.isfile(os.path.join(directory_path, item)):
            if full_path:
                file_list.append(os.path.join(directory_path, item))
            else:
                file_list.append(item)
    # 
    return file_list

# Python program to print
# colored text and background
def strRed(skk):         return "\033[91m {}\033[00m".format(skk);
def strGreen(skk):       return "\033[92m {}\033[00m".format(skk);
def strYellow(skk):      return "\033[93m {}\033[00m".format(skk);
def strLightPurple(skk): return "\033[94m {}\033[00m".format(skk);
def strPurple(skk):      return "\033[95m {}\033[00m".format(skk);
def strCyan(skk):        return "\033[96m {}\033[00m".format(skk);
def strLightGray(skk):   return "\033[97m {}\033[00m".format(skk);
def strBlack(skk):       return "\033[98m {}\033[00m".format(skk);
def strBold(skk):        return "\033[1m {}\033[0m".format(skk);

# Method to get nearest strikes
def round_nearest(x,num=50): return int(math.ceil(float(x)/num)*num)
def nearest_strike_bnf(x): return round_nearest(x,100)
def nearest_strike_nf(x): return round_nearest(x,50)


# Urls for fetching Data
url_oc      = "https://www.nseindia.com/option-chain"
url_bnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
url_nf      = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
url_indices = "https://www.nseindia.com/api/allIndices"


# Headers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br'}

sess = requests.Session()
cookies = dict()

# Local methods
def set_cookie():
    request = sess.get(url_oc, headers=headers, timeout=5)
    cookies = dict(request.cookies)

def get_data(url):
    set_cookie()
    response = sess.get(url, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==401):
        set_cookie()
        response = sess.get(url_nf, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==200):
        return response.text
    return ""

def set_header():
    global bnf_ul
    global nf_ul
    global bnf_nearest
    global nf_nearest
    response_text = get_data(url_indices)
    data = json.loads(response_text)
    for index in data["data"]:
        if index["index"]=="NIFTY 50":
            nf_ul = index["last"]
            print("nifty")
        if index["index"]=="NIFTY BANK":
            bnf_ul = index["last"]
            print("banknifty")
    bnf_nearest=nearest_strike_bnf(bnf_ul)
    nf_nearest=nearest_strike_nf(nf_ul)

# Showing Header in structured format with Last Price and Nearest Strike

def print_header(index="",ul=0,nearest=0):
    print(( index.ljust(12," ") + " => ")+ (" Last Price: ") + (str(ul)) + (" Nearest Strike: ") + (str(nearest)))

def print_hr():
    print(("|".rjust(70,"-")))


def getOptionChainData(optionChainDF, instrument, option_type, expiry_date):
    """
    getOptionChainData(optionChainDF, instrument='BANKNIFTY', option_type='CE', expiry_date='28-Jul-2022')
    instrument = 'BANKNIFTY'
    expiry_date = '25-Aug-2022'
    """
    if instrument == 'NIFTY':
        step_size  = NIFTY_STEP_SIZE
        step_count = NIFTY_STEP_COUNT
        ltp = NIFTY_LTP
    # 
    if instrument == 'BANKNIFTY':
        step_size = BANKNIFTY_STEP_SIZE
        step_count = BANKNIFTY_STEP_COUNT
        ltp = BANKNIFTY_LTP
    # 
    return optionChainDF[(optionChainDF['instrument']==instrument) & \
                  (optionChainDF['expiryDate']==expiry_date) & \
                  (optionChainDF['optionType']==option_type) & \
                  (optionChainDF['strikePrice'] >= ltp-(step_size*step_count)) & \
                  (optionChainDF['strikePrice'] <= ltp+(step_size*step_count))
                ]
    #

def getOptionChainDataFiltered(optionChainDF, instrument=None, option_type=None, expiry_date=None, strike_price=None):
    """

    instrument = 'BANKNIFTY'
    option_type = 'CE'
    expiry_date = '29-Sep-2022'
    strike_price = 40000

    getOptionChainData(optionChainDF)
    getOptionChainData(optionChainDF, strike_price=40000)
    getOptionChainData(optionChainDF, instrument, option_type, expiry_date, strike_price)
    """
    _instrument   = optionChainDF.instrument == instrument    if instrument   is not None else optionChainDF.instrument == optionChainDF.instrument
    _expiry_date  = optionChainDF.expiryDate == expiry_date   if expiry_date  is not None else optionChainDF.expiryDate == optionChainDF.expiryDate
    _option_type  = optionChainDF.optionType == option_type   if option_type  is not None else optionChainDF.optionType == optionChainDF.optionType
    _strike_price = optionChainDF.strikePrice == strike_price if strike_price is not None else optionChainDF.strikePrice == optionChainDF.strikePrice
    # 
    return optionChainDF[(_instrument) & (_option_type) & (_expiry_date) & (_strike_price)].copy()


def getOptionChainStrikePriceData(optionChainDF, instrument, strike_price):
    """
    getOptionChainStrikePriceData(optionChainDF, instrument='BANKNIFTY', strike_price=42500)
    optionChainDF = fetchNseOptionChainData()
    instrument = 'BANKNIFTY'
    expiry_date = '29-Sep-2022'
    """
    return optionChainDF[(optionChainDF['instrument']==instrument) & \
                  (optionChainDF['strikePrice'] == strike_price)]


def getOptionChainExpiryDateData(optionChainDF, instrument, expiry_date):
    """
    getOptionChainExpiryDateData(optionChainDF, instrument='BANKNIFTY', expiry_date='29-Sep-2022')
    optionChainDF = fetchNseOptionChainData()
    instrument = 'BANKNIFTY'
    expiry_date = '29-Sep-2022'

    getOptionChainStrikePriceData(getOptionChainExpiryDateData(optionChainDF, instrument='BANKNIFTY', expiry_date='29-Sep-2022'),
        instrument='BANKNIFTY', strike_price=42500)
    """
    return optionChainDF[(optionChainDF['instrument']==instrument) & \
                  (optionChainDF['expiryDate'] == expiry_date)]



global NIFTY_STEP_SIZE
global NIFTY_STEP_COUNT
global BANKNIFTY_STEP_SIZE
global BANKNIFTY_STEP_COUNT
global NIFTY_LTP
global BANKNIFTY_LTP

NIFTY_STEP_SIZE  = 50
NIFTY_STEP_COUNT = 20
BANKNIFTY_STEP_SIZE  = 100
BANKNIFTY_STEP_COUNT = 20

def getExpiryDateOptionChainData(json_data, instrument_name, expiry_date=None):
    """
    optionChainDF = getExpiryDateOptionChainData(json_data, expiry_date=None)
    """
    import pandas as pd
    optionChainDF = pd.DataFrame()
    CE_dict = {}
    PE_dict = {}
    for json_item in json_data['records']['data']:
        if 'CE' in json_item.keys():
            CE_expiryDate           = json_item['CE']['expiryDate']
            CE_strikePrice          = json_item['CE']['strikePrice']
            CE_openInterest         = json_item['CE']['openInterest']
            CE_changeinOpenInterest = json_item['CE']['changeinOpenInterest']
            CE_impliedVolatility    = json_item['CE']['impliedVolatility']
            CE_change               = json_item['CE']['change']
            CE_totalTradedVolume    = json_item['CE']['totalTradedVolume']
            CE_lastPrice            = json_item['CE']['lastPrice']
            # 
            CE_dict['optionType'] = 'CE'
            CE_dict['instrument']      = instrument_name
            CE_dict['expiryDate']           = CE_expiryDate
            CE_dict['strikePrice']          = CE_strikePrice
            CE_dict['openInterest']         = CE_openInterest
            CE_dict['changeinOpenInterest'] = CE_changeinOpenInterest
            CE_dict['impliedVolatility']    = CE_impliedVolatility
            CE_dict['change']               = CE_change
            CE_dict['totalTradedVolume']    = CE_totalTradedVolume
            CE_dict['lastPrice']            = CE_lastPrice
            # 
            optionChainDF = pd.concat([optionChainDF, pd.DataFrame(CE_dict, index=[0])])
        # 
        if 'PE' in json_item.keys():
            PE_expiryDate           = json_item['PE']['expiryDate']
            PE_strikePrice          = json_item['PE']['strikePrice']
            PE_openInterest         = json_item['PE']['openInterest']
            PE_changeinOpenInterest = json_item['PE']['changeinOpenInterest']
            PE_impliedVolatility    = json_item['PE']['impliedVolatility']
            PE_change               = json_item['PE']['change']
            PE_totalTradedVolume    = json_item['PE']['totalTradedVolume']
            PE_lastPrice            = json_item['PE']['lastPrice']
            # 
            PE_dict['optionType'] = 'PE'
            PE_dict['instrument']      = instrument_name
            PE_dict['expiryDate']           = PE_expiryDate
            PE_dict['strikePrice']          = PE_strikePrice
            PE_dict['openInterest']         = PE_openInterest
            PE_dict['changeinOpenInterest'] = PE_changeinOpenInterest
            PE_dict['impliedVolatility']    = PE_impliedVolatility
            PE_dict['change']               = PE_change
            PE_dict['totalTradedVolume']    = PE_totalTradedVolume
            PE_dict['lastPrice']            = PE_lastPrice
            # 
            optionChainDF = pd.concat([optionChainDF, pd.DataFrame(PE_dict, index=[0])])
    # 
    optionChainDF = optionChainDF.astype({'openInterest': int, 'changeinOpenInterest': int})
    return optionChainDF.reset_index().drop(['index'], axis=1)


def fetchNseOptionChainData():
    """
    """
    import pandas as pd
    from datetime import datetime
    global url_nf
    global url_bnf
    global NIFTY_LTP
    global BANKNIFTY_LTP
    # 
    nf_response_text = get_data(url_nf)
    nf_data = json.loads(nf_response_text)
    NIFTY_LTP = nf_data['records']['underlyingValue']
    # 
    bnf_response_text = get_data(url_bnf)
    bnf_data = json.loads(bnf_response_text)
    BANKNIFTY_LTP = bnf_data['records']['underlyingValue']
    # 
    optionChainDF = pd.DataFrame()
    optionChainDF = pd.concat([optionChainDF, getExpiryDateOptionChainData(json_data=nf_data, instrument_name='NIFTY')]) 
    optionChainDF = pd.concat([optionChainDF, getExpiryDateOptionChainData(json_data=bnf_data, instrument_name='BANKNIFTY')])
    optionChainDF['fetchTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 
    return optionChainDF

def printDataFrame(dataFrame, tablefmt='fancy_grid'):
    """
    """
    from tabulate import tabulate
    print(tabulate(dataFrame, headers=dataFrame.columns.values, tablefmt='psql'))
    # print(tabulateqqq(dataFrame, tablefmt=tablefmt))


def getLastThrusdayOfTheMonth():
    """
    """
    from datetime import datetime
    from dateutil.relativedelta import relativedelta, TH
    today_date = datetime.today()
    current_month = today_date.month
    # 
    for i in range(1, 6):
        t = today_date + relativedelta(weekday=TH(i))
        if t.month != current_month:
            # since t is exceeded we need last one which we can get by subtracting -2 since it is already a Thursday.
            t = t + relativedelta(weekday=TH(-2))
            break
    return t.strftime('%d-%b-%Y')


def getUpcomingThrusday():
    """
    """
    from datetime import datetime
    from dateutil.relativedelta import relativedelta, TH
    today_day=datetime.today()
    upcoming_thrusday=today_day+relativedelta(weekday=TH)
    return upcoming_thrusday.strftime('%d-%b-%Y')


def tryConvertStringToDate(date_string, output_date_format='%Y-%m-%d'):
    """
    Trying to convert string to datw with all possible combinations.
    tryConvertStringToDate(date_string='2022-09-22', output_date_format='%Y-%m-%d')
    """
    from datetime import datetime
    matching_date_format = [
        '%Y-%m-%d', # 2022-09-29
        '%Y%m%d',   # 20220929
        '%y-%m-%d', # 22-09-29
        '%y%m%d',   # 220929
        '%Y-%b-%d', # 2022-Sep-29
        '%Y%b%d',   # 2022Sep29
        '%d-%b-%Y', # 29-Sep-2022
    ]
    for date_format in matching_date_format:
        try:
            return datetime.strptime(date_string, date_format).strftime(output_date_format)
        except:
            pass
    # 
    raise Exception('Error converting {0} into datetime'.format(date_string))


def loadAllFilesFromDiskIntoDataFrame(directory_path):
    """
    directory_path = r'F:\SoftwareInstalled\Dropbox\Dropbox\Trading\TradingData\OptionChainData\20220922'
    """
    import pandas as pd
    _optionChainDF_combined = pd.DataFrame()
    for file_name in fetchAllFilesinDirectory(directory_path=directory_path):
        _optionChainDF = loadCSVFileFromDirectoryIntoDataFrame(file_name)
        _optionChainDF_combined = pd.concat([_optionChainDF_combined, _optionChainDF])
    return _optionChainDF_combined


def fetchAndSaveNseOptionChainData(expiry_date, option_type):
    """
    optionChainDF = nseOptionChainMain(expiry_date=expiry_date, option_type=args.option_type)
    """
    import os
    import time
    from datetime import datetime
    directory_path = os.path.join(DROPBOX_TRADING_OPTION_CHAIN_DATA_DIR, datetime.now().strftime('%Y%m%d'))
    end_time   = '15:35:00'
    current_time = datetime.now().strftime("%H:%M:%S")
    # 
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    # 
    # while (current_time <= end_time):
    while(true):
        try:
            optionChainDF = fetchNseOptionChainData()
            saveDataFrameToDisk(dataframe_to_save=optionChainDF, directory_path=directory_path, file_extension='csv')
            printDataFrame(getOptionChainData(optionChainDF, instrument='NIFTY', option_type=option_type, expiry_date=expiry_date))
            printDataFrame(getOptionChainData(optionChainDF, instrument='BANKNIFTY', option_type=option_type, expiry_date=expiry_date))
            print()
            print('BANKNIFTY_LTP:', BANKNIFTY_LTP)
            print('NIFTY_LTP    :', NIFTY_LTP)
            time.sleep(300)
            current_time = datetime.now().strftime("%H:%M:%S")
        except Exception as e:
            print(e)
            time.sleep(2)
    # 

# def plotGraph(optionChainDF, instrument, expiry_date, option_type, strike_price):
def plotOptionDataGraph(instrument, expiry_date, strike_price_CE, strike_price_PE):
    """
    plotOptionDataGraph(instrument='BANKNIFTY', expiry_date='27-Oct-2022', option_type='CE', strike_price_CE=40000, strike_price_PE=38000)
    """
    # 
    import os
    from datetime import datetime
    import pandas as pd
    #
    directory_path = os.path.join(DROPBOX_TRADING_OPTION_CHAIN_DATA_DIR, datetime.now().strftime('%Y%m%d'))
    _optionChainDF = loadAllFilesFromDiskIntoDataFrame(directory_path=directory_path)
    optionChainDF_1 =  getOptionChainDataFiltered(optionChainDF=_optionChainDF, expiry_date=expiry_date, option_type='CE', strike_price=strike_price_CE)
    optionChainDF_2 =  getOptionChainDataFiltered(optionChainDF=_optionChainDF, expiry_date=expiry_date, option_type='PE', strike_price=strike_price_PE)
    # 
    # print(optionChainDF_1)
    # print(optionChainDF_2)
    # 
    optionChainDF_merged = pd.merge(optionChainDF_1, optionChainDF_2, how='inner', left_on=['instrument', 'expiryDate', 'fetchTime'], right_on=['instrument', 'expiryDate', 'fetchTime'], suffixes=('_CE', '_PE'))
    optionChainDF_merged = optionChainDF_merged[['fetchTime', 'instrument', 'expiryDate', 
        # 'optionType_CE', 'optionType_PE'
        # 'changeinOpenInterest_CE', 'changeinOpenInterest_PE',
        'openInterest_CE', 'change_CE', 'impliedVolatility_CE', 'lastPrice_CE', 'strikePrice_CE',
        'strikePrice_PE', 'lastPrice_PE', 'impliedVolatility_PE','change_PE', 'openInterest_PE']]
    optionChainDF_merged.rename(columns = {'totalTradedVolume_CE':'volume_CE', 'totalTradedVolume_PE':'volume_PE',
                                           'openInterest_CE':'OI_CE', 'openInterest_PE':'OI_PE',
                                           'impliedVolatility_CE':'iv_CE', 'impliedVolatility_PE':'iv_PE',
                                           'changeinOpenInterest_CE':'change_OI_CE', 'changeinOpenInterest_PE':'change_OI_PE'}, inplace = True)
    printDataFrame(optionChainDF_merged)
    # 
    # 
    optionChainDF_1['fetchTime'] = optionChainDF_1['fetchTime'].apply(lambda x: ''.join(x.split(' ')[1].split(':')[:2]))
    optionChainDF_2['fetchTime'] = optionChainDF_2['fetchTime'].apply(lambda x: ''.join(x.split(' ')[1].split(':')[:2]))
    # 
    matplotlibPlot(x_axis_data_1=optionChainDF_1.fetchTime, y_axis_data_1=optionChainDF_1.lastPrice,
                           x_axis_data_2=optionChainDF_2.fetchTime, y_axis_data_2=optionChainDF_2.lastPrice,
                           # figsize_x=10, figsize_y=20,
                           y_label_1='CE -> '+str(strike_price_CE),
                           y_label_2='PE -> '+str(strike_price_PE),
                           y_data_1_color='green', y_data_2_color='red', 
                           y_label_1_color='green', y_label_2_color='red',
                        )

def NSEOptionChainMain():
    """
    """
    def userInput():
        print("\n\nChoose An Option")
        print("1. Execute -> fetchAndSaveNseOptionChainData")
        print("P. Execute -> plotOptionDataGraph")
        print("Q. Quit")
        option = input(': ').strip()
        return option
    #
    def inputElseDefault(input_text=None, default_value=None):
        input_string = input(input_text)
        if input_string == '':
            return default_value
        return input_string
    # 
    def userInputGraph():
        print("\n\nChoose An Option")
        input_dict = {}
        input_dict['instrument']   = inputElseDefault(input_text='Instrument : ' , default_value='BANKNIFTY')
        input_dict['option_type']  = inputElseDefault(input_text='OptionType : ' , default_value=None)
        input_dict['expiry_date']  = inputElseDefault(input_text='ExpireDate : ' , default_value=getUpcomingThrusday())
        input_dict['strike_price_CE'] = int(inputElseDefault(input_text='StrikePrice CE: ' , default_value=None))
        input_dict['strike_price_PE'] = int(inputElseDefault(input_text='StrikePrice PE: ' , default_value=None))
        # 
        return input_dict
    #
    while True:
        option = userInput()
        import os
        os.system('cls')
        if option.lower() == 'p' :
            input_dict = userInputGraph()
            plotOptionDataGraph(instrument=input_dict['instrument'], 
                                expiry_date=input_dict['expiry_date'],
                                option_type=input_dict['option_type'],
                                strike_price_CE=input_dict['strike_price_CE'],
                                strike_price_PE=input_dict['strike_price_PE'])
            # 
        elif option.lower() == 'q':
            exit()

if __name__ == '__main__':
    print("Module: NSEOptionChain [Direct Invocation]")
    # 
    
    import argparse
    from datetime import datetime
    # 
    parser = argparse.ArgumentParser()
    parser.add_argument('--expiry_date', '-ed', required=False, help='DD-bbb-YYYY', default=getUpcomingThrusday())
    parser.add_argument('--option_type', '-ot', required=False, help='CE/PE', default='CE')
    parser.add_argument('--run_type', '-rt', required=False, help='Manual/Auto', default='Auto')
    args = parser.parse_args()
    print(11)
    expiry_date = tryConvertStringToDate(date_string=args.expiry_date, output_date_format='%d-%b-%Y')
    print(22)
    # 
    if  args.run_type.lower() == 'auto':
        fetchAndSaveNseOptionChainData(expiry_date, option_type=args.option_type)
    elif args.run_type.lower() == 'manual':
        NSEOptionChainMain()
    #
else:
    print("Module: NSEOptionChain [Imported]")

# --------------------------------------------------------------------------------------------------

# Fetching CE and PE data based on Nearest Expiry Date
def print_oi(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                #print(strCyan(str(item["strikePrice"])) + strGreen(" CE ") + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + strRed(" PE ")+"[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                print(data["records"]["expiryDates"][0] + " " + str(item["strikePrice"]) + " CE " + "[ " + (str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + " PE " + "[ " + (str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                strike = strike + step


# Finding highest Open Interest of People's in CE based on CE data         
def highest_oi_CE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["CE"]["openInterest"] > max_oi:
                    max_oi = item["CE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi_strike

# Finding highest Open Interest of People's in PE based on PE data 
def highest_oi_PE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["PE"]["openInterest"] > max_oi:
                    max_oi = item["PE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi_strike


# set_header()
# print_hr()
# print_header("Nifty",nf_ul,nf_nearest)
# print_hr()
# print_oi(20, 100,nf_nearest,url_nf)
# print_hr()
# print_header("Bank Nifty",bnf_ul,bnf_nearest)
# print_hr()
# print_oi(10,100,bnf_nearest,url_bnf)
# print_hr()

# Finding Highest OI in Call Option In Nifty
# nf_highestoi_CE = highest_oi_CE(10,50,nf_nearest,url_nf)

# Finding Highet OI in Put Option In Nifty
# nf_highestoi_PE = highest_oi_PE(10,50,nf_nearest,url_nf)

# Finding Highest OI in Call Option In Bank Nifty
# bnf_highestoi_CE = highest_oi_CE(10,100,bnf_nearest,url_bnf)

# Finding Highest OI in Put Option In Bank Nifty
# bnf_highestoi_PE = highest_oi_PE(10,100,bnf_nearest,url_bnf)


# print((str("Major Support in Nifty:")) + str(nf_highestoi_CE))
# print((str("Major Resistance in Nifty:")) + str(nf_highestoi_PE))
# print((str("Major Support in Bank Nifty:")) + str(bnf_highestoi_CE))
# print((str("Major Resistance in Bank Nifty:")) + str(bnf_highestoi_PE))