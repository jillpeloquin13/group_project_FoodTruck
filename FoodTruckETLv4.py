
import pandas as pd
import requests
from pandas.io.json import json_normalize
from sqlalchemy import create_engine



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


    merged_df  = pd.concat([BosData,TalData,Vandata])
    merged_df =  merged_df.reset_index()

    merged_df.columns = ['Foodtruck', 'Time', 'Display_name', 'Lat', 'Long', 'Location']
    rds_connection_string = "postgres:postgres@localhost:5432/FoodTruck_db"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    data.to_sql(name='citydata', con=engine, if_exists='replace', index=False)
    
    return merged_df

