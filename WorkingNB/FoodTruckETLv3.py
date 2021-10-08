
import pandas as pd
import requests
from pandas.io.json import json_normalize

def getdata():

    url = 'http://data.streetfoodapp.com/1.1/schedule/vancouver'

    data =  requests.get(url).json()
    dfVan = pd.DataFrame.from_dict(data)
    dfVan.head()

    url = 'http://data.streetfoodapp.com/1.1/schedule/vancouver'
    data =  requests.get(url).json()
    data = data.vendors.apply(pd.Series)
    data.head()

    data2 = data[['description', 'name', 'description_short', 'last']].copy()
    data2 = data2.dropna()
    data2.head()


    Vandata = data2["last"].apply(pd.Series)
    Vandata.insert(4, "Location", "Vancouver")
    Vandata.head()


    url = 'http://data.streetfoodapp.com/1.1/schedule/boston'
    data =  requests.get(url).json()
    data = data.vendors.apply(pd.Series)
    data.head()

    data2 = data[['description', 'name', 'description_short', 'last']].copy()
    data2 = data2.dropna()
    data2.head()


    Bosdata = data2["last"].apply(pd.Series)
    Bosdata.insert(4, "Location", "Boston")
    Bosdata.head()


    url = 'http://data.streetfoodapp.com/1.1/schedule/tallahassee'
    data =  requests.get(url).json()
    data = data.vendors.apply(pd.Series)
    data.head()


    data2 = data[['description', 'name', 'description_short', 'last']].copy()
    data2 = data2.dropna()
    data2.head()


    Talladata = data2["last"].apply(pd.Series)
    Talladata.insert(4, "Location", "Tallahassee")
    Talladata.head()


    merged_df  = pd.concat([Bosdata,Talladata, Vandata])
    merged_df.head()

    return merged_df