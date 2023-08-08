import requests
url = "web page address"
r = requests.get(url)
htmlContent = r.content



FNO_stock_list = ['AARTIIND'    ,'ABB'         ,'ABBOTINDIA'  ,'ABCAPITAL'   ,'ABFRL'       ,'ACC'         ,'ADANIENT'    ,'ADANIPORTS'  ,'ALKEM'       ,'AMBUJACEM'   ,'APOLLOHOSP'  ,'APOLLOTYRE'  ,'ASHOKLEY'    ,'ASIANPAINT'  ,'ASTRAL'      ,'ATUL'        ,'AUBANK'      ,'AUROPHARMA'  ,'AXISBANK'    ,'BAJAJ-AUTO'  ,'BAJAJFINSV'  ,'BAJFINANCE'  ,'BALKRISIND'  ,'BALRAMCHIN'  ,'BANDHANBNK'  ,'BANKBARODA'  ,'BATAINDIA'   ,'BEL'         ,'BERGEPAINT'  ,'BHARATFORG'  ,'BHARTIARTL'  ,'BHEL'        ,'BIOCON'      ,'BOSCHLTD'    ,'BPCL'        ,'BRITANNIA'   ,'BSOFT'       ,'CANBK'       ,'CANFINHOME'  ,'CHAMBLFERT'  ,'CHOLAFIN'    ,'CIPLA'       ,'COALINDIA'   ,'COFORGE'     ,'COLPAL'      ,'CONCOR'      ,'COROMANDEL'  ,'CROMPTON'    ,'CUB'         ,'CUMMINSIND'  ,'DABUR'       ,'DALBHARAT'   ,'DEEPAKNTR'   ,'DELTACORP'   ,'DIVISLAB'    ,'DIXON'       ,'DLF'         ,'DRREDDY'     ,'EICHERMOT'   ,'ESCORTS'     ,'EXIDEIND'    ,'FEDERALBNK'  ,'FSL'         ,'GAIL'        ,'GLENMARK'    ,'GMRINFRA'    ,'GNFC'        ,'GODREJCP'    ,'GODREJPROP'  ,'GRANULES'    ,'GRASIM'      ,'GUJGASLTD'   ,'HAL'         ,'HAVELLS'     ,'HCLTECH'     ,'HDFC'        ,'HDFCAMC'     ,'HDFCBANK'    ,'HDFCLIFE'    ,'HEROMOTOCO'  ,'HINDALCO'    ,'HINDCOPPER'  ,'HINDPETRO'   ,'HINDUNILVR'  ,'HONAUT'      ,'IBULHSGFIN'  ,'ICICIBANK'   ,'ICICIGI'     ,'ICICIPRULI'  ,'IDEA'        ,'IDFC'        ,'IDFCFIRSTB'  ,'IEX'         ,'IGL'         ,'INDHOTEL'    ,'INDIACEM'    ,'INDIAMART'   ,'INDIGO'      ,'INDUSINDBK'  ,'INDUSTOWER'  ,'INFY'        ,'INTELLECT'   ,'IOC'         ,'IPCALAB'     ,'IRCTC'       ,'ITC'         ,'JINDALSTEL'  ,'JKCEMENT'    ,'JSWSTEEL'    ,'JUBLFOOD'    ,'KOTAKBANK'   ,'L&TFH'       ,'LALPATHLAB'  ,'LAURUSLABS'  ,'LICHSGFIN'   ,'LT'          ,'LTIM'        ,'LTTS'        ,'LUPIN'       ,'M&M'         ,'M&MFIN'      ,'MANAPPURAM'  ,'MARICO'      ,'MARUTI'      ,'MCDOWELL-N'  ,'MCX'         ,'METROPOLIS'  ,'MFSL'        ,'MGL'         ,'MOTHERSON'   ,'MPHASIS'     ,'MRF'         ,'MUTHOOTFIN'  ,'NATIONALUM'  ,'NAUKRI'      ,'NAVINFLUOR'  ,'NESTLEIND'   ,'NMDC'        ,'NTPC'        ,'OBEROIRLTY'  ,'OFSS'        ,'ONGC'        ,'PAGEIND'     ,'PEL'         ,'PERSISTENT'  ,'PETRONET'    ,'PFC'         ,'PIDILITIND'  ,'PIIND'       ,'PNB'         ,'POLYCAB'     ,'POWERGRID'   ,'PVR'         ,'RAIN'        ,'RAMCOCEM'    ,'RBLBANK'     ,'RECLTD'      ,'RELIANCE'    ,'SAIL'        ,'SBICARD'     ,'SBILIFE'     ,'SBIN'        ,'SHREECEM'    ,'SHRIRAMFIN'  ,'SIEMENS'     ,'SRF'         ,'SUNPHARMA'   ,'SUNTV'       ,'SYNGENE'     ,'TATACHEM'    ,'TATACOMM'    ,'TATACONSUM'  ,'TATAMOTORS'  ,'TATAPOWER'   ,'TATASTEEL'   ,'TCS'         ,'TECHM'       ,'TITAN'       ,'TORNTPHARM'  ,'TORNTPOWER'  ,'TRENT'       ,'TVSMOTOR'    ,'UBL'         ,'ULTRACEMCO'  ,'UPL'         ,'VEDL'        ,'VOLTAS'      ,'WHIRLPOOL'   ,'WIPRO'       ,'ZEEL'        ,'ZYDUSLIFE']

from bs4 import BeautifulSoup as bs
import requests

url = "https://www.moneycontrol.com/markets/earnings/results-calendar/?classic=true"

r = requests.get(url)

htmlContent = r.content

soup = bs(htmlContent, 'html.parser')

table = soup.tbody

tr_list = table.find_all('tr')

# To save HTML content
import requests
url = "https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_15_05_2023.txt"
r = requests.get(url)
htmlContent = r.content
with open('fnoinstrument1.csv', 'wb+') as f:
    f.write(htmlContent.content)



def getNameOfStock(href, verbose=0):
    """
    getNameOfStock(href='https://www.moneycontrol.com/india/stockpricequote/miningminerals/20microns/2M')
    getNameOfStock(href='')
    """
    try:
        r = requests.get(href)
        htmlContent = r.content
        soup = bs(htmlContent, 'html.parser')
        comp_info = soup.find(class_ = "comp_inf company_slider")
        print(comp_info) if verbose >= 1 else None
        #
        li_list = comp_info.find_all('li')
        details = li_list[32]
        print(details) if verbose >= 1 else None
        #
        p_list = details.find_all('p')
        name_p = str(p_list[0])
        name = name_p[3:-4]
        return name
    except Exception as e:
        print(e) if verbose >=1 else None
        return e



def getDateOfStock(td, verbose=0):
    td = str(td)
    initial_index = td.find('>')
    sliced_td = td[initial_index+1:]
    final_index = sliced_td.find('<')
    date = sliced_td[:final_index]
    print('date:', date) if verbose >= 1 else None
    return date

def checkBlankString(string):
    if string == '':
        raise Exception('Blank String Found')
    return string

def getNameAndDate(tr_list, verbose=0):
    """
    getNameAndDate(tr_list, verbose=0)
    """
    stock_dict = {}
    for tr in tr_list:
        try:
            instrument_link = checkBlankString(tr.findAll('a')[0].get("href"))
            instrument_date = checkBlankString(tr.findAll('td')[1].string)
            instrument_nse_name = checkBlankString(getNameOfStock(href=instrument_link))
            print(instrument_link, instrument_date, instrument_nse_name) if verbose >=1 else None
            stock_dict[instrument_nse_name] = instrument_date
        except Exception as e:
            print(e) if verbose >= 1 else None
            pass
        # 
    return stock_dict

def sortDictionaryByValues(dict):
    from collections import OrderedDict
    import numpy as np
    keys = list(dict.keys())
    values = list(dict.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    return sorted_dict

def getDateOfFnoStock(FNO_stock_list, tr_list, verbose=0):
    """
    getDateOfFnoStock(FNO_stock_list=FNO_stock_list, tr_list=tr_list, verbose=0)
    """
    FNO_stock_dict = {}
    all_stock_dict = getNameAndDate(tr_list=tr_list, verbose=verbose)
    for stock in FNO_stock_list:
        try:
            FNO_stock_dict[stock] = all_stock_dict[stock]
            print(stock) if verbose >= 1 else None
        except Exception as e:
            print(e) if verbose >= 1 else None
            pass
    FNO_stock_sorted_dict = sortDictionaryByValues(dict=FNO_stock_dict)
    return FNO_stock_sorted_dict

# To download instrument tokens
"""
equity tokens URL =   https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_15_05_2023.txt
fno tokens URL =   https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_11_05_2023.txt
"""

import requests
url = "https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_11_05_2023.txt"
r = requests.get(url)
htmlContent = r.content
with open('fnoinstrument1', 'wb+') as f:
    f.write(htmlContent.content)

