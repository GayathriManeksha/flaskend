from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS
from pymongo import MongoClient
import os

# os.environ['MONGO_URI'] = 'mongodb+srv://GayathriManeksha:Gaya3@cluster0.anlc4cj.mongodb.net/?retryWrites=true&w=majority'
# os.environ['MONGO_DB_NAME'] = 'mydatabase'
mongodb_password = os.environ.get('MONGODB_PASSWORD')
print("HEY____________________________")
print(mongodb_password)

client = MongoClient("mongodb+srv://GayathriManeksha:Gaya3@cluster0.anlc4cj.mongodb.net/?retryWrites=true&w=majority")
db = client.mydatabase

# from flask_login import LoginManager

app = Flask(__name__)   
CORS(app)

from app import routes