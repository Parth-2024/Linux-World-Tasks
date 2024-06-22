import pymongo as mg
myClient=mg.MongoClient("mongodb://localhost:27017/")
mydb=myClient["myPYDatabase"]#a new database has been created
print(myClient.list_database_names())
dblist=myClient.list_database_names()
if "myPYDatabase" in dblist:
    print("Database exists")
else:
    print("Database isn't showing up in the DBlist may be you need to create a collection in it first, if it doesn't have any")
mycol=mydb["Visitors"]#it will create a collection
#inplace of mydb.create_collection("Visitors") we can directly use mycol
#or
# mycol=mydb.create_collection("Visitor") we can use this code too

print(mydb.list_collection_names())
data={"name":"Parth","age":19,"degree":"Btech","course":"GenAI-ML"}
doc=mydb["Visitors"].insert_one(data)
lst=[]
print(doc.inserted_id)#returns the id of te inserted document
for i in range(1,6):
    name=input("Name:")
    age=int(input("Age:"))
    degree=input("Degree:")
    course=input("Course:")
    data1={"name":name,"age":age,"degree":degree,"coruse":course}
    lst.append(data1)
y=mydb["Visitors"].insert_many(lst)
loc=mydb["Visitors"].find_one()
print(loc)
for i in mydb["Visitors"].find():
    print(i)
for j in mycol.find({},{"_id":0,"name":1}):
    print(j)
z=mycol.find_one({"degree":"Btech"})
mydoc=mycol.find({"age":{"$gt":19}})#$gt is an operator which specifies find function to show all the records that have age more than 19
for k in mydoc:
    print(k)
sorted_doc=mycol.find().sort("age",1)#1-> ascending order and -1 -> descending order
for l in sorted_doc:
    print(l)
mycol.update_one({"degree":"BCA"},{"$set":{"degree":"Btech"}})
mycol.update_many({"degree":"Btech"},{"$set":{"age":20}})
mycol.delete_one({"name":"Nayan"})
deleted=mycol.delete_many({"age":20})
print(deleted.deleted_count)
#mycol.drop() #deletes the whole collection
