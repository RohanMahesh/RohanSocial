import pymongo

from flask import Flask, render_template, request, redirect
app = Flask("register")
myclient = pymongo.MongoClient("mongodb+srv://Rohan_Mahesh111:miniPEKKA5%@rohanmahesh.dhyd9.mongodb.net/sports?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
myDataBase = myclient["sports"]
myCollection = myDataBase["soccer"]
#reus = {"FirstName":"Marco","LastName":"Reus","Team":"Dortmund","jersey":11}
#myCollection.insert_one(reus)
#dblist = myclient.list_database_names()
#print(dblist)

#hazard = {"FirstName":"Eden","LastName":"Hazard","Team":"Madrid","jersey":11}
#messi = {"FirstName":"Lionel","LastName":"Messi","Team":"Barcelona","jersey":10}
#ronaldo = {"FirstName":"Cristiano","LastName":"Ronaldo","Team":"Juventus","jersey":7}

# myCollection.insert_many([hazard,messi,ronaldo])

# data = myCollection.find_one()
# print(data)

# da = myCollection.find()
# for each in da:
#     print(each)
#
# anot = myCollection.find({"jersey":11})
# for each in anot:
#     print(each)


# anot = myCollection.find_one({"jersey":11})
# print(anot)

# anot = myCollection.find_one({"FirstName":"Cristiano"})
# print(anot["LastName"])

#myCollection.update_one({"FirstName":"Eden"},{"$set":{"jersey":7}})

#myCollection.delete_one({"FirstName":"Marco"})

#myCollection.update_one({"FirstName":"Cristiano"},{"$set":{"postion":"LW"}})

#ano= myCollection.find_one({"FirstName":"Cristiano"})
#print(ano["postion"])

#ano= myCollection.find_one({"FirstName":"Lionel"})
#if "postion" in ano:
    #print(ano["postion"])
#else:
    #print("This person doesnt have a position")
    #myCollection.update_one({"FirstName":"Lionel"},{"$set":{"postion":"RW"}})
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        First = request.form["Firstname"]
        Last = request.form["Lastname"]
        return "hello"
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        First = request.form["Firstname"]
        Last = request.form["Lastname"]
        Team = request.form["Team"]
        Jersey = request.form["Jersey"]
        NewPlayer = {"FirstName":First,"LastName":Last,"Team":Team,"jersey":Jersey}
        myCollection.insert_one(NewPlayer)
        return redirect("/")


app.run()
