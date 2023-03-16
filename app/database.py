from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.myprojdata
data=db.mydata
# try:
#     data.insert_one({'Message':'Hey Whats up'})
# except:
#     print("error")

val=data.find()
for v in val:
    print(v['Message'])
