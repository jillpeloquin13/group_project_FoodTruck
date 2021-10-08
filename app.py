from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import FoodTruckETLv4

# Create an instance of Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")
    

# Route to render index.html template using data from Mong
# Route that will trigger the scrape function
@app.route("/getdata")
def getdata():

    # Run the scrape function
    food_data= FoodTruckETLv4.getdata()
    f"We got some new data!<br/>"
    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
