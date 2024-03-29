
import pandas as pd
import requests
from pandas.io.json import json_normalize
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import BigInteger
from sqlalchemy.types import Integer, Text, String, DateTime

def getdata():
    url = 'http://data.streetfoodapp.com/1.1/schedule/vancouver'
    data =  requests.get(url).json()
    data2 = pd.DataFrame.from_dict(data)
    data3 = data2["vendors"].apply(pd.Series)
  
    data4 = data3[['description', 'name', 'description_short', 'last']].copy()
    data4 = data4.dropna()
    
    Vandata = data4["last"].apply(pd.Series)
    Vandata.insert(4, "Location", "Vancouver")

    url = 'http://data.streetfoodapp.com/1.1/schedule/boston'
    data =  requests.get(url).json()
    data2 = pd.DataFrame.from_dict(data)
    data3 = data2["vendors"].apply(pd.Series)
    
    data4 = data3[['description', 'name', 'description_short', 'last']].copy()
    data4 = data4.dropna()

    BosData = data4["last"].apply(pd.Series)
    BosData.insert(4, "Location", "Boston")

    url = 'http://data.streetfoodapp.com/1.1/schedule/tallahassee'
    data =  requests.get(url).json()
    data2 = pd.DataFrame.from_dict(data)
    data3 = data2["vendors"].apply(pd.Series)


    data4 = data3[['description', 'name', 'description_short', 'last']].copy()
    data4 = data4.dropna()
    

    TalData = data4["last"].apply(pd.Series)
    TalData.insert(4, "Location", "Tallahassee")
    

    merged_df  = pd.concat([BosData,TalData, Vandata])
    merged_df =  merged_df.reset_index()
 


    merged_df.columns = ['foodtruck', 'time', 'display_name', 'lat', 'long', 'location']
    

    rds_connection_string = "postgres:postgres@localhost:5432/FoodTruck_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    engine.execute('delete from citydata')
    merged_df.to_sql(name='citydata', con=engine, if_exists='append', index=False)




