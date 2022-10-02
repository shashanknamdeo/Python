# Methord 1

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



# Methord 2
# path_list= ['D:\\NotebookShare\\Material\\Python\\Projects\\NSE\\Data\\NIFTY50\\20140101_20141231.csv','D:\\NotebookShare\\Material\\Python\\Projects\\NSE\\Data\\NIFTY50\\20150101_20151231.csv']
df = pd.concat(
    map(pd.read_csv, [path_list]), ignore_index=True)
print(df)