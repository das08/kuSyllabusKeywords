import glob
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

os.chdir("syllabus")
for file in glob.glob("*.txt"):
    res = keysGen.genKeys(file)

    lectureName = res[0][0].strip()
    teacherName = res[0][1].strip()
    semester = res[0][2].strip()
    keys = res[1]

    query = {'lecturename': lectureName, 'teachername': teacherName, 'semester': semester, 'keys': keys}
    _ = collection.insert(query)
