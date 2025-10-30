#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[11]:


#Pandas Assignment 2
#Question 1
#Compute the euclidean distance between series (points) p and q, without using a packaged formula.
#eculidean distance is the squre root of the sum of squared differences

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
#Use **0.5 for square root calculation
q_1 = ((p-q)**2).sum()**0.5
print(f"The euclidean distance between p and d is {q_1}")
q_1


# In[19]:


#Question 2
#Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
#Manually assign new order of the columns to the dataframe

df = df[['c','b','a','d','e']]
#Or just swap two columns by their index
#columns = df.columns.tolist()
#columns[0], columns[2] = columns[2], columns[0]
#df = df[columns]
df


# In[27]:


#Question 3
#Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
def column_interchange(df, col1, col2):
    #Create a list of the column names
    cols = df.columns.tolist()
    #Get the index of the columns we want to interchange
    if col1 in cols and col2 in cols:
        col1_index = cols.index(col1)
        col2_index = cols.index(col2)
    #This creates a tuple of columns then change the position of certain index of the columns
    cols[col1_index], cols[col2_index] = cols[col2_index], cols[col1_index]

    return df[cols]

column_interchange(df, 'a', 'c')


# In[32]:


#Question 4
#Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.

df = pd.DataFrame(np.random.random(4)**10, columns=['random'])

#Set the presentation to be in 4 decimal float form
pd.set_option('display.float_format', '{:.4f}'.format)
df


# In[65]:


#Question 5 
#Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.

df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
#Consider rows as series. We need to calculate the euclidean distance of each row with all the other rows, then put the row number of the smallest distance to the new column
#for-loop will be suitable for repeated iteration like this

#Prepare an empty lists to hold all the values for the new columns
nearest_row = []
dist = []
#This data frame has row index labeled differently than the regular number index ('a', 'b', 'c' instead of '0','1','2'). Will first catch all the row index into a list to iterate over later
row_index = df.index
#print(row_index)
for i in row_index:
    #Use .loc() to select rows, loc() is for label-based index while iloc()is for integer-based index
    current_row = df.loc[i]
    #Set the minimum distance to infinity to start the comparison with the actual calculation
    min_distance = float('inf')
    nearest_index = None

    'd'#Make sure to exclud the row itself in the comparison
    for j in row_index:
        if i != j:
            compare_row = df.loc[j]
            distance = ((current_row-compare_row)**2).sum()**0.5
            if distance < min_distance:
                min_distance = distance
                nearest_index = j
    #append the nearest row number and distance to the column list
    nearest_row.append(nearest_index)
    dist.append(min_distance)


#Add the new column to the data frame
df['nearest_row'] = nearest_row
df['dist'] = dist

df



# In[49]:


#Question 6 
#Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.

data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }
df = pd.DataFrame(data)
df
df.corr()


# In[ ]:




