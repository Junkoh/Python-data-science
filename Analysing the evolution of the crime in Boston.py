#!/usr/bin/env python
# coding: utf-8

# # Analysing the evolution of the crime in Boston
# 
# Through this project, we will analyse the evolution of crime in Boston between 2015 and 2018 and try to find :
#  - How crimes evolved through the years.
#  - What types of crimes are most common over the years.
#  - Where are the most dangerous districts and streets through the years.
#  - Which day crimes are the most frequent over the years.
#  
#       

# ## Exploring and cleaning the data

# In[1]:


# read in the data
import pandas as pd
Crime_Boston = pd.read_csv('CrimeBoston.csv')


# In[2]:


# quick exploration og the data
Crime_Boston.head()


# In[3]:


Crime_Boston.shape


# We are going to delete some useless columns and raws

# In[4]:


# We drop these 4 columns which are useless for our analysis
Crime_Boston.drop(["SHOOTING", "Lat", "Long", "Location"], axis=1, inplace=True)


# In[5]:


# We now verify that the data is clean enough to be used properly
Crime_Boston.isnull().sum()


# In[6]:


# We delete rows with missing values for the "STREET" column
Crime_Boston.dropna(subset=["STREET"], inplace=True)


# In[7]:


Crime_Boston.shape


# ## Finding how the number of crimes evolved through years in Boston

# In[13]:


import matplotlib.pyplot as plt
for i in range(2015, 2019):
    total_crime = Crime_Boston["OFFENSE_CODE_GROUP"][Crime_Boston["YEAR"] == i].value_counts().sum()
    print("The total of crimes reported for Boston in " + str(i) + " was equal to " + str(total_crime))

number_crimes = [52106, 93399, 98155, 64542]
year = [2015, 2016, 2017, 2018]
plt.plot(year, number_crimes)
plt.xlabel("Year")
plt.ylabel("Total crimes")


# We can see that the number of crimes reported had increased significantly between 2015 and 2017 and then decreased.
# We can't say why but there were a sudden increase between 2015 and 2016, and a sudden decrease between 2017 and 2018 of the total number of crimes.

# ## Finding most common type of crimes through years in Boston

# In[9]:


for i in range(2015, 2019):
    md_district = Crime_Boston["OFFENSE_CODE_GROUP"][Crime_Boston["YEAR"] == i]
    print(i)
    print(md_district.describe())
    print("\n")


# Between 2015 and 2018 the most common type of crimes in Boston had always been "Motor Vehicle Accident Response"

# ## Finding the most dangerous district and streets in Boston through years

# In[10]:


# Finding the most dangerous districts in Boston through years.
for i in range(2015, 2019):
    md_district = Crime_Boston["DISTRICT"][Crime_Boston["YEAR"] == i]
    print(i)
    print(md_district.describe())
    print("\n")


# It seems that the most dangerous district between 2015 and 2018 had always been the B2 one.

# In[11]:


# finding most dangerous streets in Boston through years.
for i in range(2015, 2019):
    md_street = Crime_Boston["STREET"][Crime_Boston["YEAR"] == i]
    print(i)
    print(md_street.describe())
    print("\n")


# So between 2015 and 2018, it seems that the most dangerous street had always been "Washington ST"

# ## Finding the day when crimes are the most committed

# In[12]:


for i in range(2015, 2019):
    md_street = Crime_Boston["DAY_OF_WEEK"][Crime_Boston["YEAR"] == i]
    print(i)
    print(md_street.describe())
    print("\n")


# The data show that most of the crimes were commited on Friday

# Finally, through this project, we analysed the evolution of the crime in Boston between 2015 and 2018
# We found that :
# - the total number of crimes has increased and then decreased 
# - the most committed type of crimes was "Motor Vehicle Accident Response"
# - the most dangerous district was the district "B2" and the most dangerous street was Washington ST
# - the day when crimes were the most committed was Friday  

# In[ ]:




