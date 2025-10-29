#!/usr/bin/env python
# coding: utf-8

# In[115]:


#Data Cleaning - 1
#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()


# In[116]:


#use flights_data
#Question 1 How many flights were there from JFK to SLC? Int q_1
#Quick check to the data
flights_data.head(10)
#Use mask to filter all the  flights that met the description
#Here I learned that Python's operator precedence - & and | have HIGHER precedence than comparison operators like >, ==, <. So parentheses are used to clearify the conditions.
mask = (flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')
#Since mask will return a boolean value of 1 and 0, the sum will be the number of the flights that meet criteria.
q_1 = int((mask).sum())
q_1


# In[117]:


#Question 2 How many airlines fly to SLC? Should be int
# To answer this we could filter all the flights to SLC then find the number of unique value of airlines
mask2 = flights_data['dest'] == 'SLC'
flightstoSLC = flights_data[mask2]
#Count the unique value of 'carrier' using nunique()
q_2 = flightstoSLC['carrier'].nunique()
q_2


# In[118]:


#Question 3 What is the average arrival delay for flights to RDU? float
flights_data.head(10)
#Get all the flights to RDU first, then calculate the mean of the delay time using .mean()
mask3 = flights_data['dest'] == 'RDU'
flightstoRDU = flights_data[mask3]
flightstoRDU['arr_delay'].mean()
q_3 = flightstoRDU['arr_delay'].mean()
print(q_3)
#Round the answer to 1 decimal and cast it to standard float format
q_3 = float(round(q_3, 1))
q_3


# In[119]:


#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)? float
#Keep using mask to filter for the flights.
#Total flights to SEA:
mask4_1 = flights_data['dest'] == 'SEA'
flightstoSEA = flights_data[mask4_1]
#Flights to SEA that were coming from NYC airports
mask4_2 = (flightstoSEA['origin'] == 'LGA') | (flightstoSEA['origin'] == 'JFK')
#The proportion will be the sum of boolean values for NYC to SEA flights over that of total flights to 
q_4 = (mask4_2).sum() / (mask4_1).sum()
#Round the answer to 2 decimal and cast it to standard float format
q_4 = float(round(q_4, 2))
q_4


# In[120]:


#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
#Pandas have a function that could directly convert data into date form: pd.to_datetime()
#First define the data of year, month and day
flights_data['date'] = pd.to_datetime(flights_data[['year', 'month', 'day']])
#Then convert to the preferred format using .strftime()
flights_data['date_string'] = flights_data['date'].dt.strftime('%Y/%m/%d')
#Quick check
flights_data['date_string'].head()
#Then calculate the mean values of the departure delay grouped by date
average_dep_delay = flights_data.groupby('date_string')['dep_delay'].mean().reset_index()
#Rename the mean value column for clarity
average_dep_delay.columns = ['date_string', 'average_dep_delay']
average_dep_delay.head()
#Then sort the data by the average depature delays and rank from largest to smallest, then the date at the first row will be the day
average_dep_delay = average_dep_delay.sort_values('average_dep_delay', ascending= False)
q_5 = average_dep_delay['date_string'].iloc[0]
print(f'The date that has the largest average depature delay was {average_dep_delay['date_string'].iloc[0]}, an average delay of {average_dep_delay['average_dep_delay'].iloc[0]}!')
q_5


# In[121]:


#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#Basically the same like question 5, just switch to the mean of arrival delay:
average_arr_delay = flights_data.groupby('date_string')['arr_delay'].mean().reset_index()
#Rename the mean value column for clarity
average_arr_delay.columns = ['date_string', 'average_arr_delay']
average_arr_delay.head()
#Then sort the data by the average arrival delays and rank from largest to smallest, then the date at the first row will be the day
average_arr_delay = average_arr_delay.sort_values('average_arr_delay', ascending= False)
q_6 = average_arr_delay['date_string'].iloc[0]
print(f'The date that has the largest average arrival delay was {average_arr_delay['date_string'].iloc[0]}, an average delay of {average_arr_delay['average_arr_delay'].iloc[0]}!')
q_6


# In[122]:


#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
#Calculate the speed first
flights_data['speed'] = (flights_data['distance']) / (flights_data['air_time'])
#Sort the flights departing from NYC by the speed and rank from largest to smallest, then the tailnumber at the first row will be the flight
mask_7 = (flights_data['origin'] == 'LGA') | (flights_data['origin'] == 'JFK')
fastestflights = flights_data[mask_7].sort_values('speed', ascending = False)
q_7 = fastestflights['tailnum'].iloc[0]
print(f'The fastest flight departing from LGA or JFK in 2013 was flight {fastestflights['tailnum'].iloc[0]}, with a speed of {fastestflights['speed'].iloc[0]}.')
q_7


# In[123]:


#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
#Just use .fillna(0) to replace nulls with 0, inplace-True very important to make sure the changes were applied to the original dataframe
weather_data_pd.fillna(0, inplace = True)
#Check if there's still nan
q_8 = weather_data_pd.isnull().sum()
q_8


# In[124]:


#Question 9 How many observations were made in Feburary? Int
#Since each roll is an observation, we just need to count all the rows with '2' as the month
#Check datatype
#print(weather_data_np.dtype)
#The array was unstructured, using column indices for mask, month is the 4th column on the sheet
mask_9 = weather_data_np[:, 3] == 2
#Sum up the true boolean value of mask_9:
q_9 = int(mask_9.sum())
q_9


# In[125]:


#Question 10 What was the mean for humidity in February? Float
#Humidity is the 9th column, calculate the mean in the array of feburary observation from question 9
#There were two observation at JFK besides the majority of observation at EWR.
#I'm including the values in mean calculation since it's not specified to only calculate the humidity at EWR.
q_10 = float(np.mean(weather_data_np[mask_9][:, 8]))
q_10


# In[126]:


#Question 11 What was the std for humidity in February? Float
#Same way to select the column as question 10
#The humidity observations at JFK were also included in the calculation
q_11 = float(np.std(weather_data_np[mask_9][:,8]))
q_11


# In[ ]:




