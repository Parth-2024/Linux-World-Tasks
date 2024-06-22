import pymongo as mg
client=mg.MongoClient("mongodb://localhost:27017/")
db=client["To-Do-List"]
col=db["To_Do_List3"]
print("Welcome to PYToDo-List\n Things you can do in this app:\n1.Enter a task\n2.Mark a task as done\n3.See all you tasks\n4.Mark a task as undone\n5.Delete a task")

def enter_task(task):
    tasks=col.find()
    data={"To-Do":task,"Action":"Not Done"}
    col.insert_one(data)
    lst=list(filter(lambda x:x["Action"]=="Not Done",col.find({},{"_id":0})))
    for i in range(0,len(lst)):
        print(lst[i]["To-Do"], ":",lst[i]["Action"])

def mark_done(task):
    lst=list(col.find({},{"_id":0}))
    count=0
    fnd=False
    while count<len(lst):
        if task == lst[count]["To-Do"]:
            print(1)
            col.update_one({"To-Do":task,"Action":"Not Done"},{"$set":{"Action":"Done"}})
            fnd=True
            break
        count+=1
    if fnd==False:
        print("Task not found")
    lst=list(col.find({},{"_id":0}))
    for i in range(0,len(lst)):
        print(lst[i]["To-Do"], ":",lst[i]["Action"])

def display_all_tasks():
    lst=list(col.find({},{"_id":0}))
    for i in range(0,len(lst)):
        print(lst[i]["To-Do"], ":",lst[i]["Action"])

def mark_undone(task):
    lst=list(col.find({},{"_id":0}))
    count=0
    fnd=False
    while count<len(lst):
        if task == lst[count]["To-Do"]:
            print(1)
            col.update_one({"To-Do":task,"Action":"Done"},{"$set":{"Action":"Not Done"}})
            fnd=True
            break
        count+=1
    if fnd==False:
        print("Task not found")
    lst=list(col.find({},{"_id":0}))
    for i in range(0,len(lst)):
        print(lst[i]["To-Do"], ":",lst[i]["Action"])

def delete_task(task):
    task=input("Enter the task you wanna delete:")
    lst=list(col.find({},{"_id":0}))
    count=0
    fnd=False
    while count<len(lst):
        if task == lst[count]["To-Do"]:
            print(1)
            col.delete_one({"To-Do":task})
            fnd=True
            break
        count+=1
    if fnd==False:
        print("Task not found")
    lst=list(col.find({},{"_id":0}))
    for i in range(0,len(lst)):
        print(lst[i]["To-Do"], ":",lst[i]["Action"])
    
choice=int(input("Enter your choice:"))
if choice==1:
    task=input("Enter your task:")
    enter_task(task)
elif choice==2:
    task=input("Enter the task you wanna mark done:")
    mark_done(task)
elif choice==3:
    display_all_tasks()
elif choice==4:
    task=input("Enter the task you wanna mark undone:")
    mark_undone(task)
elif choice==5:
    task=input("Enter the task you wanna delete:")
    delete_task(task)