#to print hello python
print("Hello Python")

#to do addition and division(operators)
num1 = int(input("num1 is: "))
num2 = int(input("num2 is: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 % num2)
print(num1 ** num2)

#find the area of a triangle
base = int(input("What is the base of your triangle: "))
height = int(input("What is the height of your triangle: "))
print(0.5 * base * height)

#a prog to swap two variables
a = input("Enter first variable: ")
b = input("Enter second variable: ")
print(f"initial values a = {a}, b = {b}")
c = a
a = b
b = c
print(f"final value of a = {a}, b= {b}")

#to generate a random number
import random

random_n = random.randint(1, 10)
print (random_n)

#to convert kilometers to meters
kilo = int(input("input your number: "))
miles = kilo * 0.621
print(f"The result from {kilo} is equal to {miles} miles")

#to convert celsius to fahrenheit
cel = int(input("Enter a temp in celsius: "))
fah = cel * (9/5) + 32
print(f"{cel} Celsius is equal to {fah}Fahrenheit")

#python prog to display calendar
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)

