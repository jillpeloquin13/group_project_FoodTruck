from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
import pandas as pd
import requests
from pandas.io.json import json_normalize
import numpy as np
from sqlalchemy import create_engine
from os import environ
from sqlalchemy.sql.sqltypes import BigInteger
from sqlalchemy.types import Integer, Text, String, DateTime
import FoodTruckETLv5



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

@app.route("/vendor")
def Vendor():
    return render_template("vendor.html")

@app.route("/vendorhistory")
def VendorHistory():
    return render_template("vendorhistory.html")
    
   


    

if __name__ == "__main__":
    app.run(debug=True)
