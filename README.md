# group_project_FoodTruck
Link to project proposal : https://emerson.bit.ai/docs/4NrJo1pXYsm4KbPp


To work with this project: 
1. Create Database schema in pgAdmin: 
    Db= FoodTruck_db
    
    CREATE TABLE citydata
(
    "Foodtruck" text,
    "Time" bigint,
    "Display_name" text,
    "Lat" double precision,
    "Long" double precision,
    "Location" text
)

2. Navigate into the repo and start the app with 'python -m flask run

3. The button 'Update Today's FoodTruck