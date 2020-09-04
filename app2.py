import pymongo
from flask import Flask, render_template, request, redirect
app = Flask("People")
myclient = pymongo.MongoClient("mongodb+srv://Rohan_Mahesh111:miniPEKKA5%@rohanmahesh.dhyd9.mongodb.net/people?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
myDataBase = myclient["people"]
myCollection = myDataBase["UserRecords"]
ActiveUser = ""

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        First = request.form["Firstname"]
        Last = request.form["Lastname"]
        Username = request.form["Username"]
        Email = request.form["Email"]
        Password = request.form["Password"]
        Confirm = request.form["Confirm"]
        Birthday = request.form["Birthday"]
        State = request.form["State"]
        if Password == Confirm:
            NewUser = {"FirstName":First,"LastName":Last,"Username":Username,"Email":Email,"Password":Password,"Birthday":Birthday,"State":State,"LoggedIn":False}
            myCollection.insert_one(NewUser)
        else:
            print('Passwords do not match')
            return redirect("/register")

        return redirect("/")


@app.route("/",methods=["GET","POST"])
def login():
    global ActiveUser
    if request.method == "GET":
        return render_template("login.html")
    else:
        username=request.form["UserName"]
        Password = request.form["Password"]
        person = myCollection.find_one({"Username":username})
        print(person)
        if person == None:
            return redirect("/register")
        else:
            if Password == person["Password"]:
                myCollection.update_one({"Username":username},{"$set":{"LoggedIn":True}})

                return redirect("/home?username="+username)
            else:
                print("Incorrect password")
                return redirect("/")

@app.route("/home",methods=["GET","POST"])
def home():

    username = request.args.get("username")
    if username is None:
        return redirect("/")
    print(username)
    person = myCollection.find_one({"Username": username})
    if request.method =="GET":
        if "LoggedIn" in person:
            if person["LoggedIn"]==True:
                if "Status" in person:
                    StatusList = person["Status"]
                    return render_template("home.html", ActiveUser=username, Status=StatusList)
                else:
                    StatusList = "No Status Available"
                    return render_template("home.html",ActiveUser=username,Status=StatusList)
            else:
                return redirect("/")
        else:
            myCollection.update_one({"Username": username}, {"$set": {"LoggedIn": False}})
            print("Something went wrong")
            return redirect("/")
    if request.method =="POST":
        newStatus=request.form["StatusBox"]
        if "Status" in person:
            StatusList = person["Status"]
            StatusList.append(newStatus)
            myCollection.update_one({"Username": username}, {"$set": {"Status": StatusList}})
        else:
            StatusList=[]
            StatusList.append(newStatus)
            myCollection.update_one({"Username": username}, {"$set": {"Status": StatusList}})
        return redirect("/home?username="+username)



@app.route("/logout")
def logout():
    username = (request.args.get("username"))
    myCollection.update_one({"Username": username}, {"$set": {"LoggedIn": False}})
    return redirect("/")




app.run()

