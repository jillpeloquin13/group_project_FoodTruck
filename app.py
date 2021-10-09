from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from pandas.core.indexing import _LocationIndexer
from sqlalchemy import create_engine
import pandas as pd
import requests
from pandas.io.json import json_normalize
import numpy as np
from os import environ
from sqlalchemy.sql.sqltypes import BigInteger
from sqlalchemy.types import Integer, Text, String, DateTime
import json
import FoodTruckETLv5
import psycopg2
import sys, os
from sqlalchemy.ext.automap import automap_base



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
def City():
    return render_template("city.html")

@app.route("/api/city")
def apicity():
    rds_connection_string = 'postgres:postgres@localhost:5432/FoodTruck_db'
    engine = create_engine(f'postgresql://{rds_connection_string}')
    

# reflect an existing database into a new model
    Base = automap_base()
# reflect the tables
    Base.prepare(engine, reflect=True)





    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Passenger.name).all()

    

    session.close()
   
    Boston_data = []
    for Foodtruck, Display_name, Lat, Long, Location in data:
        boston_dict = {}
        boston_dict["Foodtruck"] = Foodtruck
        boston_dict["Display_name"] = Display_name
        boston_dict["Lat"] = Lat
        boston_dict["Long"] = Long
        boston_dict["Location"] = Location
        Boston_data.append(boston_dict)
    return jsonify(boston_dict)

@app.route("/vendor")
def Vendor():
    return render_template("vendor.html")

@app.route("/vendorhistory")
def VendorHistory():
    return render_template("vendorhistory.html")



if __name__ == "__main__":
    app.run(debug=True)
