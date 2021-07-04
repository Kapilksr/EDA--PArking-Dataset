#!/usr/bin/env python
# coding: utf-8

# In[1]:


## import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[2]:


## read the data
data=pd.read_excel('Parking.xls')


# In[3]:


## eyeball the data
df=data
df.head()


# In[4]:


## to check the counts and types of building status
df['Bldg Status'].value_counts()


# In[5]:


## to check the counts and types of property type
df['Property Type'].value_counts()


# In[6]:


## to check top 10 states with most number of buildings
df['Bldg State'].value_counts().head(10)


# In[7]:


## to check top 10 cities with most number of buildings
df['Bldg City'].value_counts().head(10)


# ## 1. what is the distribution for owned/leased?

# In[8]:


df.columns


# In[9]:


## we can further see the counts by pivot table option
owned_leased=pd.pivot_table(df,index='Owned/Leased',values='Total Parking Spaces')


# In[10]:


owned_leased


# In[11]:


## we see that by default it shows us the mean value we can change it
owned_leased=pd.pivot_table(df,index='Owned/Leased',values='Total Parking Spaces',aggfunc='count')
owned_leased


# In[12]:


## we can plot the bar chart for this
owned_leased.plot(kind='bar')
plt.show()


# ## 2. In which states the parking situation is in excess

# In[13]:


df.head()


# In[14]:


excess_buildings=pd.pivot_table(df,index='Bldg State',columns='Bldg Status',values='Total Parking Spaces')


# In[15]:


excess_buildings


# In[16]:


## we see that there are many NaN values in excess columns so we remove them
excess_buildings=excess_buildings[excess_buildings['EXCESS']>0]


# In[17]:


excess_buildings


# In[18]:


# we can put them on the graph

excess_buildings.plot(kind='bar',figsize=(10,8))
plt.show()


# In[19]:


# but as per the question we need only EXCESS buildings with order


# In[20]:


plt.bar(excess_buildings.index,excess_buildings['EXCESS'])
plt.show()


# In[21]:


## but we need it sorted


# In[22]:


excess_buildings_sorted=excess_buildings['EXCESS'].sort_values(ascending=False)
excess_buildings_sorted


# In[23]:


plt.figure(figsize=(10,7))
plt.bar(excess_buildings_sorted.index,excess_buildings_sorted.values)
plt.show()


# ## 3. Building cities that have been decommissioned along with total parking

# In[24]:


df.head()


# In[25]:


## we can filter the data 
decom=df[df['Bldg Status']=='DECOMMISSIONED']
decom


# In[26]:


## we see only two cities where parking spaces have been decommissioned


# In[27]:


decom=df[(df['Bldg Status']=='DECOMMISSIONED') & (df['Total Parking Spaces']>0)]
decom


# ## 4. In which type of property the parking spaces are in excess?
# 

# In[28]:


excess_prop=pd.pivot_table(df[df['Bldg Status']=='EXCESS'],index='Property Type',values='Total Parking Spaces')
excess_prop


# ## 5. Where are more number of active parkings available- Owned/Leased

# In[31]:


active_parking=pd.pivot_table(df[df['Bldg Status']=='ACTIVE'],index='Owned/Leased', values='Total Parking Spaces')
active_parking


# # 5. states with more number of leased parkings

# In[33]:


more_leased=pd.pivot_table(df[df['Owned/Leased']=='LEASED'],index='Bldg City', values='Total Parking Spaces')
more_leased.sort_values('Total Parking Spaces',ascending=False)


# ## 6. Which property type has more active parking?

# In[34]:


df.head()


# In[35]:


more_active=pd.pivot_table(df[df['Bldg Status']=='ACTIVE'],index='Property Type',values='Total Parking Spaces')
more_active


# In[37]:


## we scan plol this as
more_active.plot(kind='bar')
plt.show()


# In[38]:


## clearly structure property type has more parking spaces


# ## 7. How is the distribution of parking in city by property type?

# In[40]:


dis_prop=pd.pivot_table(df,index='Bldg City',columns='Property Type',values='Total Parking Spaces')
dis_prop


# ## 8. Building states that have zero parking spaces.

# In[41]:


df.columns


# In[42]:


zero_park=df[df['Total Parking Spaces']==0]
zero_park


# In[45]:


states_zero=zero_park.groupby(['Bldg State'])['Total Parking Spaces'].sum()
states_zero


# In[46]:


# above mentioned states are the states with zero parking spaces


# ## 9. Which states have max and min parking spaces

# In[49]:


space=df.groupby(['Bldg State'])['Total Parking Spaces'].sum()
space


# In[54]:


space_sorted=space.sort_values(ascending=False)
space_sorted


# In[60]:


## max parking space
space_sorted.head(1)


# In[61]:


# min parking space
space_sorted.tail(1)


# In[ ]:




