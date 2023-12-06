import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#Retriving the "ID" column and assifning it to a variable x

x=df[['ID']]
print(x)
print(type(x))
'''
# Access to multiple columns
# Let us retrieve the data for Department, Salary and ID columns

# Retrieving the Department, Salary and ID columns and assigning it to a variable z
​'''
z = df[['Department','Salary','ID']]
print(z)

students = {'Student':['David', 'Samuel', 'Terry', 'Evan'], 'Age':[27,24,22,32],'Country':['UK', 'Canada', 'China','USA'], 'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 'Marks': [85,72,89,76]} 
df1=pd.DataFrame(students)
print(df1)

b = df1[['Marks']]
print(b)

c = df1[['Country', 'Course']]
print(c)

# To view the column as a series, just use one bracket

x = df1['Student']
print(x)
print(type(x))
