# 1 #to print hello python
# print("Hello Python")

# 2 #to do addition and division(operators)
# num1 = int(input("num1 is: "))
# num2 = int(input("num2 is: "))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 % num2)
# print(num1 ** num2)

# 3 #find the area of a triangle
# base = int(input("What is the base of your triangle: "))
# height = int(input("What is the height of your triangle: "))
# print(0.5 * base * height)

# 4 #a prog to swap two variables
# a = input("Enter first variable: ")
# b = input("Enter second variable: ")
# print(f"initial values a = {a}, b = {b}")
# c = a
# a = b
# b = c
# print(f"final value of a = {a}, b= {b}")

# 5 #to generate a random number
# import random

# random_n = random.randint(1, 10)
# print (random_n)

# 6 #to convert kilometers to miles
# kilo = int(input("input your number: "))
# miles = kilo * 0.621
# print(f"The result from {kilo} is equal to {miles} miles")

# 7 #to convert celsius to fahrenheit
# cel = int(input("Enter a temp in celsius: "))
# fah = cel * (9/5) + 32
# print(f"{cel} Celsius is equal to {fah}Fahrenheit")

# 8 #python prog to display calendar
# import calendar

# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# cal = calendar.month(year, month)
# print(cal)

# #9 write a python program to solve quadratic equation
# #formular is ax2 + bx + c = 0

# a = int(input("input your value for a: "))
# b = int(input("input your value for b: "))
# c = int(input("input your value for c: "))

# #note:a,b,c are real numbers
# dis = b**2 - 4*a*c
# #if dis is positive, negative or zero
# if dis > 0:
#    root1 = (-b + (dis**0.5)) / (2*a)
#    root2 = (-b - (dis**0.5)) / (2*a)
#    print(f"Root 1: {root1}")
#    print(f"Root 2: {root2}")
# elif dis == 0:
#     root = -b/(2*a)
#     print(f"Root: {root}")
# else:
#     root3 = (-b + (dis**0.5)) / (2*a)
#     root4 = (-b - (dis**0.5)) / (2*a)
#     print(f"Root 1: {root3}")
#     print(f"Root 2: {root4}")

# # writing a python program to swap two variables without using an extra variable
# a = 10
# b = 15
# print(f"The value of a is {a} and the value of b is {b}")
# a,b = b,a
# print(f"The value of a is {a} and the value of b is {b}")

# #Write a Python Program to Check if a Number is Positive, Negative or Zero

# num = int(input("input any number of your choice: "))
# if num < 0:
#     print(f"{num} is a negative number")

# elif num == 0:
#     print(f"{num} is zero")

# else:
#     print(f"{num} is a negative number")

# # Write a Python Program to Check if a Number is Odd or Even
# numb = int(input("input a number of your choice: "))

# if numb % 2 == 0:
#     print(f"{numb} is an even number")
# else:
#     print(f"{numb} is an odd number")

# # Write a Python Program to Check Leap Year
# year = int(input("Input any year of your choice: "))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# # Write a Python Program to Check Prime Number
# num1 = int(input("input a number of your choice: "))
# #defining a flag variable
# flag = False

# if num1 == 1:
#     print(f"{num1}, is not a prime number")
# elif num1 > 1:
#     for i in range(2, num1):
#         if (num1 % i) == 0:
#             flag = True #if factor exist, set flag to True:
#             break
# if flag:
#     print(f"{num1} is not a prime number")
# else:
#     print(f"{num1} is a prime number")

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10
lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")
for num2 in range(lower, upper + 1):
    #all prime numbers are greater than 1

   