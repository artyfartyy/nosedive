import json, os
Obama = True
def createUser():
    err = False
    user = input("username: ").upper()
    passwd = input("password: ")
    for i in os.listdir("users"):
        if f"{user}.json" == i:
            err = True
    if err == True:
        print("ERROR: user already exists o algo")
    else:
        sixseven = len(os.listdir("users"))
        da = {"id": sixseven, "username": user, "password": passwd, "isadmin": False}
        with open(f"users/{user}.json", "w") as a:
            json.dump(da, a, indent=3)

def login():
    global Obama
    user = input("Enter your username: ").upper()
    password = input("Enter your password: ")
    if f"{user}.json" in os.listdir("users"):
        with open(f"users/{user}.json", "r") as maslow:
            if password == json.load(maslow)["password"]:
                print("login success!")
                Obama = False
                with open("isloggedin.json", "w") as schweinefleisch:
                    aaa = {"isloggedin": True, "loggedinuser": user}
                    json.dump(aaa, schweinefleisch, indent=3)
            else:
                print("bruh something went wrong")
    else:
        print("bruh something else went wrong")

def userPathCheck():
    #Checking whether or not the users path exists.
    pathdebug=False
    if os.path.isdir("users")==True:
        if pathdebug==True:
            print("the path already exists")
    else:
        if pathdebug==True:
            print("false")
        os.mkdir("users")
        if os.path.isdir("users")==True and pathdebug==True:
            print("created the path")
        elif pathdebug==True:
            print("error creating the path")

def cookieCheck():
    if os.path.exists("isloggedin.json") == False:
        with open("isloggedin.json", "w") as ui:
            json.dump({"isloggedin": False, "loggedinuser": "temporary"}, ui, indent=3)
    else:
        print("all good!")

def MainOp():
    userPathCheck()
    cookieCheck()
    with open("isloggedin.json", "r") as BigMac:
        HijoDePuta = json.load(BigMac)
    if HijoDePuta["isloggedin"] == False:
        hello = input("""
        (1) CREATE USER
        (2) LOGIN
        \n""")
        if hello == "1":
            createUser()
        elif hello == "2":
            login()
        else:
            print("Bro, you had ONE JOB!")
    else:
        Gogol = HijoDePuta["loggedinuser"]
        print("You're already logged in!")
        print(f"Welcome back {Gogol}")


while Obama:
    MainOp()
    idk = input("Do you want to do something? [Y/N]: ")
    if idk.upper() == "N":
        Obama = False
