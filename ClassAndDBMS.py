import pymongo as mg
myClient=mg.MongoClient("mongodb://localhost:27017/")
class Visitor:
    def __init__(self,client,dbname,col_name):
        self.myclient=client
        self.db=self.myclient[dbname]
        self.col=self.db[col_name]
    def insert_doc(self,name,age,crt_sts):
        doc={"Name":name,"Age":age,"Current_Status":crt_sts}
        docs=self.col.insert_one(doc)
        return docs.inserted_id
    def read_docs(self):
        for i in self.col.find():
            print(i)
dbname=input("Enter the db name:")
col_name=input("Enter the collectio name:")
VisitorForm1=Visitor(myClient,dbname,col_name)
while True:
    name=input("Name:")
    age=int(input("Age:"))
    crt_sts=input("Current Status:")
    id=VisitorForm1.insert_doc(name,age,crt_sts)
    print(f"This is your id:{id}")
    if input("Do you want to add more docs:")=="N":
        break
VisitorForm1.read_docs()