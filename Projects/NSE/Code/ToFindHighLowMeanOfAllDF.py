
import sys
PYTHON_LIB_FILEIO_DIR = r'D:\NotebookShareAsus\Material\Python\PythonLibrary\FileIO'
sys.path.append(PYTHON_LIB_FILEIO_DIR)

from LibFetchFileNameFromDisk import toFetchAllFilesinDirectory

def toFindHighLowMean(data_path):
    import pandas as pd
    # High-Low mean
    instrumentDF = pd.read_csv(data_path)
    #
    instrumentDF['high-low_percent'] = (abs(instrumentDF['high']-instrumentDF['low'])/instrumentDF['low'])*100
    return instrumentDF['high-low_percent'].mean()

def toSaveMeanOfAllDFInDict(path):
    #  r"D:\NotebookShareAsus\Material\Python\Projects\NSE\Data\Daily_data"
    import os 
    file_name_list = os.listdir(path)
    file_path_list = toFetchAllFilesinDirectory(path)
    mean_dict={}
    for i in range(0,len(file_name_list)):
        mean=toFindHighLowMean(file_path_list[i])
        name_temp=file_name_list[i]
        length=len(name_temp)
        name=name_temp[slice(len(name_temp)-4)]
        mean_dict[name]=mean
    return mean_dict


