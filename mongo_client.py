from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.hi

collection = db.test

myCPU = {"use": "dsfsadfgsd"}
post_id = collection.insert_one(myCPU).inserted_id
