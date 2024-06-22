import pymongo as mg
from bson.objectid import ObjectId
client=mg.MongoClient("mongodb://localhost:27017/")
class Database:
    def __init__(self,client):
        self.client=client
    def dblist(self):
        print(self.client.list_database_names())
    def get_db(self,dbName):
        self.db=self.client[dbName]
        return self.db
    def col_list(self):
        print(self.db.list_collection_names())

class Admin(Database):
    password=12345678
    def __init__(self,col_name,db,dbname,password):
        self.db=db.get_db(dbname)
        self.col=self.db[col_name]
        if Admin.password==password:
            print("Welcome")
        else:
            print("Wrong password")

    def store(self):
        lst=[]
        while True:
            self.name=input("Name:")
            self.age=int(input("Age:"))
            self.crt_sts=input("Current Status:")
            self.info={
                "Name":self.name,
                "Age":self.age,
                "Current_Status":self.crt_sts
            }
            lst.append(self.info)
            if input("Do you want to keep adding records:")=="N":
                break
        self.col.insert_many(lst)
    def find(self):
        res=input("Do you want me to show a specific record:")
        if res=="Y":
            self.id=input("Enter the id:")
            fnd=self.col.find_one({"_id":ObjectId(self.id)})
            if fnd:
                print("Found:",fnd)
            else:
                print("Id doesn't exist")
        else:
            if input("Do you wnat me to show all the ids:")=="Y":
                lst=self.col.find()
                for i in lst:
                    print(i)
            else:
                lmt=int(input("Enter the limit:"))
                lst=self.col.find().limit(lmt)
                for i in lst:
                    print(i)

    def delt(self):
        self.res=input("Do you want to delete all the records:")
        if self.res=="Y":
            rcds=self.col.delete_many({})
            print(rcds.deleted_count,"accounts deleted")
        else:
            key=input("Enter the field:")
            val=input("Enter the value:")
            rcds=self.col.delete_many({key:ObjectId(val)})
            print("Accounts Deleted:",rcds.deleted_count)
    
    def update(self):
        key=input("Enter the field you want to update:")
        val=input("Enter the value with which you wanna update it:")
        self.res=input("Do you want me to update all the records:")
        if self.res=="Y":
            ud=self.col.update_many({},{"$set":{key:val}})
        else:
            key_main=input("Enter the specific parameter:")
            val_main=input("Enter the value:")
            ud=self.col.update_one({key_main:ObjectId(val_main)},{"$set":{key:val}})
        print(f"Accounts Updated:{ud.modified_count}")

class User(Database):
    def __init__(self,col_name,db,db_name):
        self.db=db.get_db(db_name)
        self.col=self.db[col_name]
    def insert(self):
        self.name=input("Name:")
        self.age=int(input("Age:"))
        self.crt_sts=input("Current Status:")
        self.data={
            "Name":self.name,
            "Age":self.age,
            "Current_Status":self.crt_sts
        }
        self.id=self.col.insert_one(self.data)
        print("Your Id:",self.id.inserted_id)
    def search(self,id):
        self.id=ObjectId(id)
        lst=self.col.find_one({"_id":self.id})
        if lst:
            print(lst)
        else:
            print("User not found")
    def update(self,id,field,field_data):
        lst=self.col.find_one({"_id":ObjectId(id)})
        if lst:
            lst=self.col.update_one({"_id":ObjectId(id)},{"$set":{f"{field}":f"{field_data}"}})
            lst=self.col.find_one({"_id":ObjectId(id)})
            print("Updated:",lst)
        else:
            print("User not found")
    def delete(self,id):
        lst=self.col.find_one({"_id":ObjectId(id)})
        if lst:
            self.col.delete_one({"_id":ObjectId(id)})
            print("deleted")
        else:
            print("User not found")

server=Database(client)
server.dblist()
db=input("Program Name:")
server.get_db(db)
res=input("Are you a User or an Admin:")
if res=="User":
    server.col_list()
    col=input("Collection:")
    user=User(col,server,db)
    choice=int(input("The operation you can perform:\n1.For Sign In\n2.For Search\n3.For Update\n4.Delete\nEnter your choice:"))
    if choice==1:
        user.insert()
    elif choice==2:
        id=input("Id:")
        user.search(id)
    elif choice==3:
        id=input("Id:")
        field=input("Enter the field you want to update:")
        val=input("Enter the info with which you wanna update it:")
        user.update(id,field,val)
    elif choice==4:
        id=input("Id:")
        user.delete(id)
    else:
        print("Invalid choice")
elif res=="Admin":
    password=int(input("Password:"))
    server.col_list()
    col=input("Collection:")
    admin=Admin(col,server,db,password)
    choice=int(input("The operation you can perform:\n1.For Sign In\n2.For Search\n3.For Update\n4.Delete\nEnter your choice:"))
    if choice==1:
        admin.store()
    elif choice==2:
        admin.find()
    elif choice==3:
        admin.update()
    elif choice==4:
        admin.delt()
    else:
        print("Invalid Choice")
    
    
    
    
