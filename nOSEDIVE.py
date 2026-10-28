import json, os

def createUser():
    err = False
    user = input("username: ")
    passwd = input("password: ")
    for i in os.listdir("users"):
        if f"{user}.json" == i:
            err = True
    if err == True:
        print("ERROR: user already exists o algo")
    else:
        sixseven = len(os.listdir("users"))
        da = {"id": sixseven, "username": user.upper(), "password": passwd, "isadmin": False}
        with open(f"users/{user.upper()}.json", "w") as a:
            json.dump(da, a, indent=3)

def login():
    user = input("Enter your username: ").upper()
    password = input("Enter your password: ")
    if f"{user}.json" in os.listdir("users"):
        with open(f"users/{user}.json", "r") as maslow:
            if password == json.load(maslow)["password"]:
                print("login success!")

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