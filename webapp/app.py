from flask import Flask, render_template
import pandas as pd
import os
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import feedparser
from sqlalchemy.orm import Session

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Connect to Database (Ensure the engine ready to go for use in endpoints)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','')
db = SQLAlchemy(app)

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(db.engine, reflect=True)

# Save references to each table
#ml_table = Base.classes.ml_predict

####################### END POINTS #######################

# END POINT: HOME
@app.route("/")
def home():

    # Return template and data
    return render_template("index.html")

# END POINT: Data Story 
@app.route("/datastory")
def story():

    # Return template and data
    return render_template("datastory.html")

# END POINT: Data Story 
@app.route("/machinelearning")
def ml():

    # Return template and data
    return render_template("machinelearning.html")

############################################################

@app.route("/Diesavgmetro")
def diesavmetro():

    rawrss = ['https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?StateRegion=98&Product=4']

    dies = pd.DataFrame([])

    for url in rawrss:
        dp = feedparser.parse(url)

        for i, e in enumerate(dp.entries):
            one_feed = {}
            one_feed['Price'] = e.price if 'price' in e else f'price {i}'
            one_feed['Address'] = e.address if 'address' in e else f'no address {i}'
            one_feed['Phone'] = e.phone if 'phone' in e else f'phone {i}'
            dies = dies.append(pd.DataFrame([one_feed]), ignore_index=True)
        
    dies['Price'] = pd.to_numeric(dies['Price'])
    dies_mean = pd.DataFrame(dies.mean(), columns=['Average ULP Perth Metro'])
    dies_mean = dies_mean['Average ULP Perth Metro'].round(2)
    dies_mean = dies_mean.to_json(orient='values')
    
    return dies_mean

@app.route("/ULPavgmetro")
def ulpavmetro():

    rawrss = ['https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?StateRegion=98&Product=1']

    ulp_metro = pd.DataFrame([])

    for url in rawrss:
        dp = feedparser.parse(url)

        for i, e in enumerate(dp.entries):
            one_feed = {}
            one_feed['Price'] = e.price if 'price' in e else f'price {i}'
            one_feed['Address'] = e.address if 'address' in e else f'no address {i}'
            one_feed['Phone'] = e.phone if 'phone' in e else f'phone {i}'
            ulp_metro = ulp_metro.append(pd.DataFrame([one_feed]), ignore_index=True)
        
    ulp_metro['Price'] = pd.to_numeric(ulp_metro['Price'])
    ulp_mean = pd.DataFrame(ulp_metro.mean(), columns=['Average ULP Perth Metro'])
    ulp_mean = ulp_mean['Average ULP Perth Metro'].round(2)
    ulp_mean = ulp_mean.to_json(orient='values')
    
    return ulp_mean

@app.route("/bestulpmetro")
def bestprice():

    rawrss = ['https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?StateRegion=98&Product=1']

    best_metro_ulp_price = pd.DataFrame([])

    for url in rawrss:
        dp = feedparser.parse(url)

        for i, e in enumerate(dp.entries):
            one_feed = {}
            one_feed['Price'] = e.price if 'price' in e else f'price {i}'
            one_feed['Brand'] = e.brand if 'brand' in e else f'price {1}'
            one_feed['Address'] = e.address if 'address' in e else f'no address {i}'
            one_feed['Phone'] = e.phone if 'phone' in e else f'phone {i}'
            best_metro_ulp_price = best_metro_ulp_price.append(pd.DataFrame([one_feed]), ignore_index=True)
    
    best_metro_ulp_price['Price'] =pd.to_numeric(best_metro_ulp_price['Price'])
    best_metro_ulp_price = best_metro_ulp_price.nsmallest(1, 'Price')
    best_metro_ulp_price = best_metro_ulp_price.nsmallest(1,'Price').drop(columns=['Address', 'Phone'])
    top_1 = best_metro_ulp_price.to_json(orient='values')

    return top_1

@app.route("/bestDLpmetro")
def bestDLprice():

    rawrss = ['https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?StateRegion=98&Product=4']

    best_metro_dl_price = pd.DataFrame([])

    for url in rawrss:
        dp = feedparser.parse(url)

        for i, e in enumerate(dp.entries):
            one_feed = {}
            one_feed['Price'] = e.price if 'price' in e else f'price {i}'
            one_feed['Brand'] = e.brand if 'brand' in e else f'price {1}'
            one_feed['Address'] = e.address if 'address' in e else f'no address {i}'
            one_feed['Phone'] = e.phone if 'phone' in e else f'phone {i}'
            best_metro_dl_price = best_metro_dl_price.append(pd.DataFrame([one_feed]), ignore_index=True)
    
    best_metro_dl_price['Price'] =pd.to_numeric(best_metro_dl_price['Price'])
    best_metro_dl_price = best_metro_dl_price.nsmallest(1, 'Price')
    best_metro_dl_price = best_metro_dl_price.nsmallest(1,'Price').drop(columns=['Address', 'Phone'])
    top_1 = best_metro_dl_price.to_json(orient='values')
    print(top_1)
    return top_1

@app.route("/mlpredict")
def predict():
    session = Session(db.engine)
    ml_predict = db.session.execute("""Select * from ml_predict""")
    db_data = pd.DataFrame(ml_predict, columns=[ 
        'Index', 
        'Actual', 
        'LineearReg',
        'LGBMRegressor', 
        'LinearSVR', 
        'RandomForestRegressor'])
    db_data = db_data.drop(columns=['Index'])
    table = db_data.to_json(orient='records')
    print(db_data)
    return table 

if __name__ == "__main__":
    app.run(debug=True)

