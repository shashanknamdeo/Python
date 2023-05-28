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

# To read files with desire seprator
df = pd.read_csv(file_name,sep = '|')

# To drop column 
df.drop(["column name"], axis=1)

# To slice data frame by ignore_index
df.iloc[0:4]

# To locate value of column by value of another column having same index
In [2]: df
Out[2]:
    A  B
0  p1  1
1  p1  2
2  p3  3
3  p2  4

In [3]: df.loc[df['B'] == 3, 'A']
Out[3]:
2    p3
Name: A, dtype: object

In [4]: df.loc[df['B'] == 3, 'A'].iloc[0]
Out[4]: 'p3'

# Suppose you have csv file with columns ["id", "name", "last_name"] and you want to read column ["name", "last_name"]. You can do it as below:

import pandas as pd
df = pd.read_csv("sample.csv", usecols=["name", "last_name"])

# To save dataframe
df.to_csv("file Name", header=True, index=False)


# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and
file1 = open("MyFile.txt", "w")
   
# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt", "w+")