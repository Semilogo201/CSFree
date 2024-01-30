#users first name
fname = input("What is your first name: ")
surname = input("What is your surname: ")
print(f"{fname}, {surname}")
password = "Milo"
while True:
    Milo_Password = input("input your password: \n")
    if Milo_Password == password:
        print("password successful")
        break
    else:
        print("incorrect password")