#python primitive data types
#string(comprises of characters)
# print("Hello"[4]) #subscripting- the act of pulling out an element from a string
# print("Hello"[-1])

# #integer(numbers without decimal places either positive or -ve number)
# print("123" + "456")
# print(123 + 456)
# #large numbers sep with comas can be written using _ in python
# print(123_456 + 789_123)
# #float(With decimal places)
# print(1.23 + 4.56)
# #Boolean(True or False)
# num = 1
# if num < 0:
#     print("it is a decimal number")
# elif num == 0:
#     print("num is equal to 0")
# else:
#     print("number is greater than or equal to 1")
# #Functions(some sort of machine that does some task and then returns to us an output)
# #len function does not work with integers
# num_char = len(input("What is your name?"))
# print("Your name has" + num_char + "characters.")#the output will give a type error because we a concatinating a string with an integer.
# print(type(num_char))#type checking

#type conversion(type casing)
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has"+" " + new_num_char + " " + "characters.")

#type function
# a = 123
# print(type(a))#a type integer
# a = str(123)
# print(type(a))#a type string

# print(70 + float("100.5"))#"100.5" is a string been converted top a floating point number
# print("70" + "100")
# print(str(70) + str(100))

#coding exercise
# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# #solution
# print(type(two_digit_number))
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print(int(first_digit + second_digit))

#division in python will always give a floating point number
print(type(6 / 2))
print(2 ** 2)#this means 2 the power of 3
print(3 * 8)
print(4 - 1)

#P.E.M.D.A.S.L.R (Parentheses(), Exponents**, Multiplication*, Division/, Addition+, Subtraction-, The calculation goes from left to right)
print(3*3+3/3-3) 
#changing the above line of code so i can get 3 as the output
print(3*(3+3)/3-3)

#Working on a B.M.I Calculator
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
H = float(height)
W = int(weight)
bmi = W/(H*H)
print = int(bmi)
#another way of solving it
height = float(height)
weight = int(weight)
bmi = (weight / (height*height))
print(int(bmi))

#to round up numbers in pytthon
print(round(8/3, 2))#we are planning to round it up to 2d.p this way
print(8//3)#when you want an integer not a floating point number

#variable declaration, variable initialization $ increment or decrement
score = 0

#user scores a point
score = score + 1
score += 1

print(score)
print("your score is " + str(score))#instead of lots of plus sighs
#you use the f string
print("your score is {score}")

#calculating the number of years we have in our lifetime
age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} left.")


