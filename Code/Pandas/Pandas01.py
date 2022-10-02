file_name = r'C:\Users\Notebook\Downloads\Orders\Orders01.csv'

import pandas as pd

orderDF = pd.read_csv(file_name)

# To count no. of names in row 
ordersDF.value_counts('row name')

example
ordersDF.value_counts('Type')
Type
SELL    16
BUY     11

# To see all function pandas
pd."press tab"

# For help in cmd 
help("function name")

example
help(pd.read_csv)

# To see names of a spscific type in a row
ordersDF[ordersDF."row name" == 'name']

example
ordersDF[ordersDF.Type == 'SELL']

# To merge two files in one data frame
df = pd.concat(
    map(pd.read_csv, ['mydata.csv', 'mydata1.csv']), ignore_index=True)
print(df)