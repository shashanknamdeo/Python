import sys
PYTHON_LIB_FILEIO_DIR = r'D:\NotebookShareAsus\Material\Python\PythonLibrary\FileIO'
sys.path.append(PYTHON_LIB_FILEIO_DIR)

from LibFetchFileNameFromDisk import toFetchAllFilesinDirectory

def toAppendDataframe(path_list):
    # path_list= ['D:\\NotebookShare\\Material\\Python\\Projects\\NSE\\Data\\NIFTY50\\20140101_20141231.csv','D:\\NotebookShare\\Material\\Python\\Projects\\NSE\\Data\\NIFTY50\\20150101_20151231.csv']
    # FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead
    import pandas as pd
    df1 = pd.DataFrame()
    for element in path_list:
        df2=pd.read_csv(element)
        df_new=pd.concat([df1,df2],ignore_index=True)
        df1=df_new
    return df1

def loadHistoricalDataFromDisk(instrument_name, path):
    """
    instrument_name='NIFTY50'
    instrumentDF = loadHistoricalDataFromDisk(instrument_name=instrument_name, path=path)
    """
    # path=r'D:\NotebookShareAsus\Material\Python\Projects\NSE\Data'
    import os
    full_path=os.path.join(path,instrument_name)
    files_path=toFetchAllFilesinDirectory(full_path)
    data_frame=toAppendDataframe(files_path)
    return data_frame







instrumentDF = loadHistoricalDataFromDisk(instrument_name=instrument_name, path=path)
instrumentDF['close-open'] = instrumentDF['Close']-instrumentDF['Open']
instrumentDF['close-open_percent'] = (abs(instrumentDF['Close']-instrumentDF['Open'])/instrumentDF['Open'])*100
instrumentDF['close-open_percent'].describe()


instrumentDF['high-low'] = instrumentDF['High']-instrumentDF['Low']
instrumentDF['high-low_percent'] = (abs(instrumentDF['High']-instrumentDF['Low'])/instrumentDF['Low'])*100
instrumentDF['high-low_percent'].describe()




