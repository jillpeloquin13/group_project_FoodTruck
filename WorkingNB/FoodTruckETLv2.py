import pandas as pd
import requests


def getdata():

    url = 'http://data.streetfoodapp.com/1.1/schedule/vancouver'
    data =  requests.get(url).json()
    dfVan = pd.DataFrame.from_dict(data)
    dfVan.head()

    url = 'http://data.streetfoodapp.com/1.1/schedule/boston'
    data=  requests.get(url).json()
    dfBos = pd.DataFrame.from_dict(data)
    dfBos.head()

    url = 'http://data.streetfoodapp.com/1.1/schedule/tallahassee'
    data=  requests.get(url).json()
    dfTalla = pd.DataFrame.from_dict(data)
    dfTalla.head()

    return dfBos