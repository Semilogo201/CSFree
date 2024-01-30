def validate_password(fname, surname):
#password validation
#while loop (password validation)
    fname = input("What is your first name: ")
    surname = input("What is your surname: ")
#password validation
while True:
    password = input("Enter a password(Your password must contain uppercase, lowercase, digit, and special character):")
    if len(password) < 8:
        print("password must be at most 8 characters long")
    elif not any(char .isupper() for char in password):
        print("password must contain at least one upper case")
    elif not any(char.islower()for char in password):
        print("password must contain at least one lower case")
    elif not any(char.isdigit()for char in password):
        print("password must contain at least one digit")
    elif not any(char in "!@$%^&*()" for char in password):
        print(password must contain at least one special character):
    else:
        print("password is correct")
        break
