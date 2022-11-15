def toFetchAllFilesinDirectory(path):
    # path = r"D:\NotebookShare\Material\Python\Projects\NSE\Data\NIFTY50"
    import os
    dir_list = os.listdir(path)
    files_name = []
    for element in dir_list:
        if os.path.isfile(os.path.join(path,element)) :
            files_name.append(os.path.join(path,element))
    return files_name






import sys
PYTHON_LIB_FILEIO_DIR = r'D:\NotebookShareAsus\Material\Python\PythonLibrary\FileIO'
sys.path.append(PYTHON_LIB_FILEIO_DIR)

from LibFetchFileNameFromDisk import toFetchAllFilesinDirectory