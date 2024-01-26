#Data Visualization Code

#To read Excel file
#!mamba install openpyxl==3.0.9 -y

import numpy as np # useful for many scientific computing in Python
import pandas as pd # primary data structure library

#Download and read Excel file
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

#read top 5 rows of the dataset
df_can.head()
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10) 

#read bottom 5 rows of the dataset
df_can.tail()
# tip: You can specify the number of rows you'd like to see as follows: df_can.tail(10)

#This method can be used to get a short summary of the dataframe.
 df_can.info(verbose=False)

 #To get the list of column headers we can call upon the data frame's columns instance variable.
 df_can.columns

 #to get the list of indices we use the .index instance variables.
df_can.index

print(type(df_can.columns))
print(type(df_can.index))

df_can.columns.tolist()
df_can.index.tolist()

print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))

#To view the dimensions of the dataframe, we use the shape instance variable of it.
# size of dataframe (rows, columns)
df_can.shape

#Let's clean the data set to remove a few unnecessary columns. We can use pandas drop() method as follows:

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

#Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

#We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:

df_can['Total'] = df_can.sum(axis=1)
df_can['Total']

#We can check to see how many null objects we have in the dataset as follows:

df_can.isnull().sum()

#Finally, let's view a quick summary of each column in our dataframe using the describe() method.

df_can.describe()

df_can.Country  # returns a series

df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.

T#here are main 2 ways to select rows:

df.loc[label]    # filters by the labels of the index/column
df.iloc[index]   # filters by the positions of the index/column

df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()

# optional: to remove the name of the index
df_can.index.name = None

# 1. the full row data (all columns)
df_can.loc['Japan']

# alternate methods
df_can.iloc[87]

df_can[df_can.index == 'Japan']

# 2. for year 2013
df_can.loc['Japan', 2013]

# alternate method
# year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]

# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]

# Alternative Method
df_can.iloc[87, [3, 4, 5, 6, 7, 8]]

# To convert the column names into strings: '1980' to '2013'.

df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

year = list(map(str, range(1990, 2013)))
haiti = df_can.loc['Haiti', year]

'''
Filtering based on a criteria 
To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.

For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).
'''
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pass this condition into the dataFrame
df_can[condition]

# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

'''
Sorting Values of a Dataframe or Series
You can use the sort_values() function is used to sort a DataFrame or a Series based on one or more columns.
You to specify the column(s) by which you want to sort and the order (ascending or descending). Below is the syntax to use it:-

df.sort_values(col_name, axis=0, ascending=True, inplace=False, ignore_index=False)

col_nam - the column(s) to sort by.
axis - axis along which to sort. 0 for sorting by rows (default) and 1 for sorting by columns.
ascending - to sort in ascending order (True, default) or descending order (False).
inplace - to perform the sorting operation in-place (True) or return a sorted copy (False, default).
ignore_index - to reset the index after sorting (True) or keep the original index values (False, default).
'''
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5
