# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:50:18 2021

@author: dibya
"""

import pandas as pd
import numpy as np
import datetime
import pickle
import sklearn
from flask_restful import Api, Resource
from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
from datetime import date

from dash_application import create_dash_application

import json

df=pd.read_csv("bitcoin_prices_v1.csv")
df=df.to_numpy()
df=df.tolist()

    

app = Flask(__name__, template_folder="templates")
app.static_folder="static"

create_dash_application(app)

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")
@app.route("/dev.html", methods=['GET'])
@cross_origin()
def dev():
	return render_template("dev.html")

@app.route("/about.html",methods=["GET"])
@cross_origin()
def about():
	return render_template("about.html")

@app.route("/predict",methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        year=int(request.form['mintemp'])
        month=int(request.form['maxtemp'])
        day=int(request.form['rainfall'])
        d0=date(2021,6,1)
        x=date(year,month,day)
        d=x-d0
        y=d.days
        t=df[2431+y]
        output=round(t[0],2)
        
        retmap={
          'bitcoin_price':output}
        return render_template("3.html", prediction_text='Predicted Bicoin price on {0} is {1}'.format(x,output))
    return render_template("predict.html")


if __name__=='__main__':
	app.run()			 

