from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

client = MongoClient('localhost', 27017)
# from flask_login import LoginManager

app = Flask(__name__)   
CORS(app)

from app import routes