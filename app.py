from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import FoodTruckETLv3

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/FoodTruck_db")

@app.route("/")
def welcome():
    return render_template("index.html")
    

# Route to render index.html template using data from Mong
# Route that will trigger the scrape function
@app.route("/getdata")
def getdata():

    # Run the scrape function
    food_data= FoodTruckETLv3.getdata()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.insert_many(merged_df.to_dict('records'))


    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
