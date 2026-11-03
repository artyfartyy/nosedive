import json, os
Obama = True
def createUser(): 
    err = False
    user = input("username: ").upper()
    passwd = input("password: ")
    for i in os.listdir("users"): # for loop that checks if inputed user already exists.
        if f"{user}.json" == i:
            err = True
    if err == True:
        print("ERROR: user already exists o algo")
    else:
        sixseven = len(os.listdir("users")) #sixseven is set to the next unused id.
        da = {"id": sixseven, "username": user, "password": passwd, "isadmin": False}# sets a user entry in the users folder.
        with open(f"users/{user}.json", "w") as a:
            json.dump(da, a, indent=3)

def login():
    global Obama #obama is used for keeping the main operation loop going.
    user = input("Enter your username: ").upper()
    password = input("Enter your password: ")
    if f"{user}.json" in os.listdir("users"):
        with open(f"users/{user}.json", "r") as maslow:#goes through and checks through all existing users and sets it to maslow
            if password == json.load(maslow)["password"]:#checks if maslow fits with the set pasword.
                print("login success!")
                Obama = False
                with open("isloggedin.json", "w") as schweinefleisch:#creates a isloggedin cookie for next login.
                    aaa = {"isloggedin": True, "loggedinuser": user}
                    json.dump(aaa, schweinefleisch, indent=3)
            else:
                print("bruh something went wrong")
    else:
        print("bruh something else went wrong")

def userPathCheck():
    #Checking whether or not the users path exists.
    pathdebug=False #toggles printed debug texts for the path debugging
    if os.path.isdir("users")==True:#checks wether or not the path exists
        if pathdebug==True:
            print("the path already exists")
    else:
        if pathdebug==True:
            print("false")
        os.mkdir("users") #creates the user path if it doesnt exist.
        if os.path.isdir("users")==True and pathdebug==True:#checks wether or not the path was succesfully created.
            print("created the path")
        elif pathdebug==True:
            print("error creating the path")

def cookieCheck():#checks if there is a isloggedin cookie.
    if os.path.exists("isloggedin.json") == False:
        with open("isloggedin.json", "w") as ui:
            json.dump({"isloggedin": False, "loggedinuser": "temporary"}, ui, indent=3)#if cookie doesnt exist create a temporary one that isnt logged in.
    else:
        print("all good!")

def MainOp():# the main operation function.
    userPathCheck()
    cookieCheck()
    with open("isloggedin.json", "r") as BigMac:
        HijoDePuta = json.load(BigMac)
    if HijoDePuta["isloggedin"] == False:#checks if hijodeputa isnt a eligible isloggedin cookie.
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


while Obama: #the operation loop
    MainOp()
    idk = input("Do you want to do something? [Y/N]: ") #inputs yes or no to restart the operation.
    if idk.upper() == "N":
        Obama = False
