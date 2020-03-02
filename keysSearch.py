import os
from pymongo import MongoClient
import setting
import keysGen

mongo_user = os.environ.get("mongo_user")
mongo_pass = os.environ.get("mongo_pass")
mongo_host = os.environ.get("mongo_host")
mongo_port = os.environ.get("mongo_port")

uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}"
client = MongoClient(uri)

conn = client["keywordDB"]
collection = conn['keywords']

words = [
    "土地",
    "地表"
]

keySearchList = []
lecNameSearchList = []
for _ in words:
    keySearchList.append({'keys': _})
    lecNameSearchList.append({'lecturename': {'$regex': f'^(?=.*{_}).*$', '$options': 'i'}})

# query = {'$or': [{'$and': keySearchList}, {'$or': lecNameSearchList}]}
query = {'$or': [{'$and': keySearchList}]}

res = collection.find(query)
for __ in res:
    print(__["lecturename"], __["teachername"])
