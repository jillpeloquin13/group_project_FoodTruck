#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import requests
from pandas.io.json import json_normalize


# Get the schedule Data for Vancouver

# In[59]:


url = 'http://data.streetfoodapp.com/1.1/schedule/vancouver'

data =  requests.get(url).json()
dfVan = pd.DataFrame.from_dict(data)
dfVan.head()


# In[60]:


url = 'http://data.streetfoodapp.com/1.1/schedule/vancouver'
data =  requests.get(url).json()
data = df.vendors.apply(pd.Series)
data.head()


# In[61]:


data2 = data[['description', 'name', 'description_short', 'last']].copy()
data2 = data2.dropna()
data2.head()


# In[64]:


Vandata = data2["last"].apply(pd.Series)
Vandata.insert(4, "Location", "Vancouver")
Vandata.head()


# Grab Boston

# In[66]:


url = 'http://data.streetfoodapp.com/1.1/schedule/boston'
data =  requests.get(url).json()
data = df.vendors.apply(pd.Series)
data.head()


# In[67]:


data2 = data[['description', 'name', 'description_short', 'last']].copy()
data2 = data2.dropna()
data2.head()


# In[68]:


Bosdata = data2["last"].apply(pd.Series)
Bosdata.insert(4, "Location", "Boston")
Bosdata.head()


# Get the Tallahassee Data

# In[69]:


url = 'http://data.streetfoodapp.com/1.1/schedule/tallahassee'
data =  requests.get(url).json()
data = df.vendors.apply(pd.Series)
data.head()


# In[70]:


data2 = data[['description', 'name', 'description_short', 'last']].copy()
data2 = data2.dropna()
data2.head()


# In[71]:


Talladata = data2["last"].apply(pd.Series)
Talladata.insert(4, "Location", "Tallahassee")
Talladata.head()


# In[72]:


merged_df  = pd.concat([Bosdata,Talladata, Vandata])
merged_df.head()


# In[ ]:




