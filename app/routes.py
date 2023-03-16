from flask import Flask, request, flash, url_for, redirect, render_template,jsonify
from app import app
from pymongo import MongoClient
from flask_cors import cross_origin
from bson.json_util import dumps
from bson.objectid import ObjectId
# client = MongoClient('localhost', 27017)
# db=client.myprojdata
from app import db

# client = MongoClient("mongodb+srv://GayathriManeksha:Gaya3@cluster0.anlc4cj.mongodb.net/?retryWrites=true&w=majority")
# db = client.mydatabase
data=db.mydata
try:
    data.insert_one({'Message':'High'})
except:
    print("error")

@app.route('/put')
@cross_origin()
def put_val():
    val=data.find({})
    list_data=list(val)
    print(list_data)
    json_data=dumps(list_data)
    # with open('data.json', 'w') as file:
    #     file.write(json_data)
    return json_data

@app.route('/adddata',methods=['POST'])
@cross_origin()
def add_value():
    msg=request.json['Message']
    print(msg)
    data.insert_one({'Message':msg})
    return {'Name':msg}
