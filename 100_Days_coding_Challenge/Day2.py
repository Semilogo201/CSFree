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
two_digit_number = input()
# 🚨 Don't change the code above 👆
#solution
print(type(two_digit_number))
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(int(first_digit + second_digit))