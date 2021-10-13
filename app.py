from flask import Flask, render_template, redirect, jsonify, request
from flask_pymongo import PyMongo
import FoodTruckETLv5
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import numpy as np
from sqlalchemy import Column, Integer, String, Float, Text, Numeric
import simplejson as json
from decimal import Decimal
import requests
import json


## DB Connection
rds_connection_string = 'postgres:postgres@localhost:5432/FoodTruck_db'
engine = create_engine(f'postgresql://{rds_connection_string}')
    
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Citydata= Base.classes.citydata

### DB connection done

# Create an instance of Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")
    
@app.route("/getdata")
def data():
    FoodTruckETLv5.getdata()
    return redirect("/")

@app.route("/city")
def city(): 
    return render_template("city.html")

@app.route("/api/city")
def result():
    session = Session(engine)
    results = session.query(Citydata.foodtruck, Citydata.lat, Citydata.long).all()
    session.close()

    all_data= []
    for foodtruck, lat, long in results:
        city_dict = {}
        city_dict["foodtruck"] = foodtruck
        city_dict["lat"] = lat
        city_dict["long"] = long
        all_data.append(city_dict)
    
    return jsonify(all_data)


@app.route("/vendor")
def Vendor():
    return render_template("vendor.html")



@app.route('/api/vendor', methods=['GET', 'POST'])
def result2():
    r = requests.get(f'http://data.streetfoodapp.com/1.1/vendors/chickpea-truck')
    citydata=json.loads(r.text)['open']
    return jsonify(citydata)


@app.route('/api/vendor/<name>', methods=['GET', 'POST'])
def resultvendor(name):
    url = 'http://data.streetfoodapp.com/1.1/vendors/'+ name
    r = requests.get(url)
    citydata=json.loads(r.text)['open']
    return jsonify(citydata)


@app.route("/api/wordcloud")
def wordcloud():
    session = Session(engine)
    results = session.query(Citydata.display_name).all()
    session.close()
    return jsonify(results)


@app.route("/wordcloud")
def wordcloudtemp():
    return render_template("wordcloud.html")



if __name__ == "__main__":
    app.run(debug=True)


