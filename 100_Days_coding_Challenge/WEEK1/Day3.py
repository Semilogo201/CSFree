#Control flow with if/else and conditional operators
water_level = 50
if water_level > 80:
    print("drain")
else:
    print("dont drain")

  #A program that replaces a ticket box
    print("Welcome to the rollercoaster")
    height = int(input("What is your height? "))

    if height > 120:
        print("you can ride the rollercoaster!")
 #Nested if/else statement
        age = int(input("What is your age? "))
        if age < 12:
            print("Please pay $5.00")
        elif age <= 18:
            print("Please pay $7.00")
        else:
            print("Please pay $12.00")

    else:
        print("you can't ride")
    #comparison operator(<,>,>=,<=,==,!=)
    #writing a program to see if it is a odd or even number
        number = int(input())
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

#upgrading B.M.I calculator
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
  # Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("Leap year")
        else:
           print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
#Write a Python program that takes an integer as input 
#and prints whether it is positive, negative, or zero.

num = int(input("num: "))

if num < 0:
   print(f"{num} is negative")
elif num == 0:
   print(f"{num} is zero")
else:
   print(f"{num} is positive")

#Triangle Type(Write a program that takes three integer inputs representing the sides of a triangle and prints whether it's an equilateral, isosceles, or scalene triangle.)
length = int(input("what is the length: "))
base = int(input("what is the base: "))
height = int(input("what is the height: "))

if (length == base == height):
   print(length*height*base)
   print("It is an equilateral triangle")
elif (length == base != height) or (length == height != base) or (height == base != length):
    print(length*height*base)
    print("It is an isosceles triangle")
else:
    print(length*height*base)
    print("It is a scalene triangle")

#Grade Classifier:Develop a Python program that takes a student's exam score as input and prints their corresponding letter grade (A, B, C, D, or F)
Grade = int(input("Input your grade: "))
if Grade >= 70:
    print("you have an A")
elif Grade >= 60:
    print("you have a B")
elif Grade >= 50:
    print("you have a C")
elif Grade >= 40:
    print("you have a D")
elif Grade >= 30:
    print("you have an E")
else:
    print("you have an F")

#Vowel or Consonant: Write a Python script that takes a single character as input and prints whether it is a vowel or a consonant.
char = (input("input a single character: "))

if len(char) == 1: #to accertain the length of character is 1
    char = char.lower() #to accertain it will take both upper and lower case letters
    if char == "aeiou":
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")

#Ticket Price Calculator:
#Develop a program that calculates the ticket price based on the age of a person. Ask the user for their age and print the ticket price according to the following 
age = int(input("What is your age: "))

if age <= 5:
    print("Your ticket is free")
elif age <= 12:
    print("Your ticket fee is $10")
elif age <= 18:
    print("Your ticket fee is $15")
elif age <= 60:
    print("Your ticket fee is $20")
else:
    print("Your ticket fee is $10")
