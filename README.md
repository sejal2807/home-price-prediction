# home-price-prediction

Bangalore home price prediction website https://real-estate-price-prediction12.herokuapp.com/

First we will build a model by sklearn and linear regression using banglore home price dataset that has been taken form kaggle website. 

Now we will write a python flask server which is going to provide the location values and has been hosted on heroku.
https://real-estate-locations.herokuapp.com/get_location

Next step is to write the flask server as backend for estimating price and website is built in html, css and javascript which allows user to enter area square feet, number of bathrooms and bedrooms etc. Location values are fetched using jquery in javascript file.

Data cleaning, outlier detection and removal, gridsearchcv for hyperparameter tunning are used in model.
