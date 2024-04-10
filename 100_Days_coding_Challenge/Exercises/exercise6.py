#conditional statements
height = int(input("enter height in feet: "))

if (height > 3):
    print("Buy token")
else:
    print("No token required")

#to find out if a number is even or odd
number = int(input("input a number:  "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This number is an odd number")

#nested if, else and elif statements
height = int(input("what is your height: "))

if height >= 3:
    print("can ride")
    age = int(input("what is your age: "))
    if age < 12:
        print("please pay #1000")
    elif age <= 18:
        print("please pay #2500")
    else:
        print("please pay #5000")
else:
    print("you cant ride")
print("bye")