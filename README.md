# group_project_FoodTruck
Link to project proposal : https://emerson.bit.ai/docs/4NrJo1pXYsm4KbPp


To work with this project: 
1. Create Database schema in pgAdmin: 
    Db= FoodTruck_db
    
 CREATE TABLE citydata
(
    Foodtruck TEXT,
    Time NUMERIC,
    Display_name TEXT,
    Lat NUMERIC,
    Long NUMERIC,
    Location TEXT
)

Select * from citydata

ALTER TABLE citydata ADD PRIMARY KEY ("Foodtruck", "Location");

2. Navigate into the repo and start the app with 'python -m flask run

3. The button 'Update Today's FoodTruck

4. Create schemea and check

CREATE TABLE citydata
(
    Foodtruck TEXT PRIMARY KEY,
    Time NUMERIC,
    Display_name TEXT,
    Lat NUMERIC,
    Long NUMERIC,
    Location TEXT
)

Delete from citydata
