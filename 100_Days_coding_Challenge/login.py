#we are creating a sign up or sign in form for our website
#create a prompt to either sign in or sign up
#if the user chooses to sign up, collect the users informations
#if they choose to sign in, only ask for their username and password

print("welcome to tech-titans portal")
users = []

isuser_loggedin = False

while True:
    choice = input("Do you want to sign up or sign in: ")

    if choice == "sign up":
        name = input("please enter your name: ")
        username = input("Enter your desired username: ")
        email = input("enter your email: ")
        password = input("create a password: ")
        users.append({"Name": name, "Username": username, "Email":email, "Password":password})
        print(f"Hello {name}, Your account has been created!")
    break
    elif choice == "sign in":
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("enter your password: ")
    print(f"you have successfully logged in as {username}")
    
else:

