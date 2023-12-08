# To create empty dataframe
df = pd.DataFrame()

# To make a df with dictionary
details = {'Ankit' : 22,'Golu' : 21,'hacker' : 23}
pd.DataFrame(list(details.items()), columns = ['Name', 'rol_no'])

# to see full DataFrame
    # Permanently changes the pandas settings
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    
    # To Resets the options
    pd.reset_option('all')

# To see top n rows of dataframe
df.head('n')

# To slice Dataframe
df[:]

# To describe values of a perticular ColumnS
df[["column1","column2"]].describe(include="all")

# drop a column name 'A' (axis=1 for column)
df.drop(['A'], axis=1)

# To drop the column/row with null values
df.dropna()
"""
Pandas DataFrame.dropna() Syntax
Syntax: DataFrameName.dropna(axis=0, how=’any’, thresh=None, subset=None, inplace=False)

Parameters:

axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String. 
how: how takes string value of two kinds only (‘any’ or ‘all’). ‘any’ drops the row/column if ANY value is Null and ‘all’ drops only if ALL values are null.
thresh: thresh takes integer value which tells minimum amount of na values to drop. 
subset: It’s an array which limits the dropping process to passed rows/columns through list. inplace: It is a boolean which makes the changes in data frame itself if True.
"""

# To rename column name
df.rename(columns = {'test':'TEST'}, inplace = True)

# To set a colume as index
df = df.set_index("column name")

# to Convert Index to Datetime
df.index = pd.to_datetime(df.index) # Note index shoud be in formmat '4-15-2022 10:15', '5-19-2022 7:14', '8-01-2022 1:14','6-14-2022 9:45', '10-24-2022 2:58',

# get index of rows where column is equal to 7
df.index[df['points']==7].tolist()

# to get value of a column at a peticular index
df._get_value('index_no', 'column_name')

# to get full row
df.iloc['row no'] # vertically
df.iloc[['row no']] # horizontally

# to fill none value of a column wit its previous filled value
nba["College"].fillna( method ='ffill', inplace = True)

# Merge
# to merge 'Grade', 'Name' column of df2 with df1 on 'name' column
df1.merge(df2[['Grade', 'Name']], on = 'Name', how = 'left')

# to reset index and drop previous index
df.reset_index(inplace = True, drop = True)

# to get instrument token value at which instrumentName == 'instrument_name' , expiry == 'expiry_date' etc
instrument_token = token_df[(token_df.instrumentName == 'instrument_name') & (token_df.expiry == 'expiry_date') & (token_df.strike == 'strike_price') & (token_df.optionType == 'option_type')].instrumentToken.values[0]

# To get the list of index having row with none values in cloumn_1 and cloumn_2
df[(df.cloumn_1.isnull()) | (df.cloumn_2.isnull())].index.to_list()

# to view some basic statistical details like percentile, mean, std, etc. 
# Parameters: 
# percentile: list like data type of numbers between 0-1 to return the respective percentile (ex: percentiles=[.20, .40, .60, .80])
# include: List of data types to be included while describing dataframe. Default is None (ex: include=['object', 'float', 'int'])
# exclude: List of data types to be Excluded while describing dataframe. Default is None (ex: exclude=['object', 'float', 'int'])
# Return type: Statistical summary of data frame
df.describe(percentiles=None, include=None, exclude=None)
df.describe().T # rotate describe table by 90 degree

df.size    # To return size of dataframe/series which is equivalent to total number of elements. That is rows x columns.
df.shape   # To return tuple of shape (Rows, columns) of dataframe/series
df.ndim    # To Returns dimension of dataframe/series. 1 for one dimension (series), 2 for two dimension (dataframe)

# To find the co-relation between columns of DataFrame
df.corr()

# To find difference between column values
df.Close.diff(periods = 1, axis=1)
