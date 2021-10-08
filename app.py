from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
import FoodTruckETLv4

# Create an instance of Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")
    

# Route to render index.html template using data from Mong
# Route that will trigger the scrape function
@app.route("/getdata")
def data():
    f"We got some new data!<br/>"
    # Run the scrape function
    FoodTruckETLv4.getdata()

    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
