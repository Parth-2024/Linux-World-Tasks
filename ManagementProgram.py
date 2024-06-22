import pymongo as mg
myClient=mg.MongoClient("mongodb://localhost:27017/")
mydb=myClient["myPYDatabase"]
mycol=mydb["Visitors2"]
for docs in mycol.find({},{"_id":0}):
    print(docs)