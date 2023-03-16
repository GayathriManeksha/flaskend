from pymongo import MongoClient

import os

os.environ['MONGO_URI'] = 'mongodb+srv://GayathriManeksha:Gaya3@cluster0.anlc4cj.mongodb.net/?retryWrites=true&w=majority'
os.environ['MONGO_DB_NAME'] = 'mydatabase'

client = MongoClient(os.environ.get('MONGO_URI'))
db = client[os.environ.get('MONGO_DB_NAME')]
data=db.mydata

val=data.find()
for v in val:
    print(v['Message'])
