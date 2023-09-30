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

# drop a column name 'A'
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