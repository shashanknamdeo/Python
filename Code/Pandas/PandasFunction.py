# to see full DataFrame

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

# To Resets the options
pd.reset_option('all')

# To see top n rowsof dataframe
df.head('n')

# To slice Dataframe
df[:]

# To describe values of a perticular ColumnS
df[["column1","column2"]].describe(include="all")