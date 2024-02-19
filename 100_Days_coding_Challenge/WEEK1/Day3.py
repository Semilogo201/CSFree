# #Control flow with if/else and conditional operators
# water_level = 50
# if water_level > 80:
#     print("drain")
# else:
#     print("dont drain")

#   #A program that replaces a ticket box
#     print("Welcome to the rollercoaster")
#     height = int(input("What is your height? "))
#     bill = 0
#     if height > 120:
#         print("you can ride the rollercoaster!")
#  #Nested if/else statement
#         age = int(input("What is your age? "))
#         if age < 12:
#             bill = 5
#             print("child's ticket is 5")
#         elif age <= 18:
#            bill = 7
#            print("Youth ticket is 7")
#         else:
#             bill = 12
#             print("Adult ticket is 12")
#         photo = (input("Would you like to take photos with your ticket? y/n: "))
#         if photo == 'y':
#           bill = bill + 3 #or bill+= 3
#         print(f"Your final bill is {bill}")
#     else:
#         print("you can't ride")
#     #comparison operator(<,>,>=,<=,==,!=)
#     #writing a program to see if it is a odd or even number
#         number = int(input())
#     if number % 2 == 0:
#         print("This is an even number.")
#     else:
#         print("This is an odd number.")

# #upgrading B.M.I calculator
# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")

# #Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
#   # Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#            print("Leap year")
#         else:
#            print("Not Leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")
# #Write a Python program that takes an integer as input 
# #and prints whether it is positive, negative, or zero.

# num = int(input("num: "))

# if num < 0:
#    print(f"{num} is negative")
# elif num == 0:
#    print(f"{num} is zero")
# else:
#    print(f"{num} is positive")

# #Triangle Type(Write a program that takes three integer inputs representing the sides of a triangle and prints whether it's an equilateral, isosceles, or scalene triangle.)
# length = int(input("what is the length: "))
# base = int(input("what is the base: "))
# height = int(input("what is the height: "))

# if (length == base == height):
#    print(length*height*base)
#    print("It is an equilateral triangle")
# elif (length == base != height) or (length == height != base) or (height == base != length):
#     print(length*height*base)
#     print("It is an isosceles triangle")
# else:
#     print(length*height*base)
#     print("It is a scalene triangle")

# #Grade Classifier:Develop a Python program that takes a student's exam score as input and prints their corresponding letter grade (A, B, C, D, or F)
# Grade = int(input("Input your grade: "))
# if Grade >= 70:
#     print("you have an A")
# elif Grade >= 60:
#     print("you have a B")
# elif Grade >= 50:
#     print("you have a C")
# elif Grade >= 40:
#     print("you have a D")
# elif Grade >= 30:
#     print("you have an E")
# else:
#     print("you have an F")

# #Vowel or Consonant: Write a Python script that takes a single character as input and prints whether it is a vowel or a consonant.
# char = (input("input a single character: "))

# if len(char) == 1: #to accertain the length of character is 1
#     char = char.lower() #to accertain it will take both upper and lower case letters
#     if char == "aeiou":
#         print(f"{char} is a vowel")
#     else:
#         print(f"{char} is a consonant")

# #Ticket Price Calculator:
# #Develop a program that calculates the ticket price based on the age of a person. Ask the user for their age and print the ticket price according to the following 
# age = int(input("What is your age: "))

# if age <= 5:
#     print("Your ticket is free")
# elif age <= 12:
#     print("Your ticket fee is $10")
# elif age <= 18:
#     print("Your ticket fee is $15")
# elif age >= 45 and age <= 55:
#     print("Everything is going to be okay. Your ticket is free")
# elif age <= 60:
#     print("Your ticket fee is $20")
# else:
#     print("Your ticket fee is $10")

# #Building an Automatic Pizza Order

# print("Thank you for choosing Python Pizza Deliveries!")
# bill = 0
# size = input("What size of pizza will you like to order?, S,M,L: ")
# add_pepperoni = input("Would you like some pepperoni? Y/N: ")
# extra_cheese = input("and some extra cheese? Y/N: ")
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1
# print(f"Your final bill is: ${bill}.")

# #logical operators (and: the two conditions have to be true, Or: at least one condition has to be true,)
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# names = name1 + name2
# Lnames = names.lower()
# t = Lnames.count("t")
# r = Lnames.count("r")
# u = Lnames.count("u")
# e = Lnames.count("e")
# first_digit = t+r+u+e
# l = Lnames.count("l")
# o = Lnames.count("o")
# v = Lnames.count("v")
# e = Lnames.count("e")
# second_digit = l+o+v+e
# score =  int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

#working on a treasure island game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You\'re at a cross road, where will you like to go, 'left' or 'right'? ").lower()

if choice1 == 'left':
    #Continue in the game.
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across").lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow, one blue Which color do you choose?").lower()
    #game will continue
        if choice3 == 'red':
            print("it is a room full of fire. game over.")
        elif choice3 == 'yellow':
            print("you found the tresure, you win")
        elif choice3 == 'blue':
            print("you entered a room of beast. game over.")
        else:
            print("you chose a door that doesnt exist. game over")
    else:
        print("you get attacked by an angry trout. game over")
else:
    print("Game Over.")
