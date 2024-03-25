# """Cases in python are Camel Case (Each word, except the first, starts with a capital letter:myVariableName = "John"), Pascal Case(Each word starts with a capital letter):
# MyVariableName = "John", Snake Case(Each word is separated by an underscore character:my_variable_name = "John", """
# """Unpack a Collection(If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking. e.g Unpack a list:

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)) """

# """Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables."""
# # #Create a variable outside of a function, and use it inside the function
# # x = "awesome"

# # def myfunc(): #function declaration
# #   print("Python is " + x)

# # myfunc() #called function

# # #Create a variable inside a function, with the same name as the global variable(local declaration of variables)
# # x = "awesome"

# # def myfunc():
# #   x = "fantastic"
# #   print("Python is " + x)

# # myfunc()

# # print("Python is " + x)
# #when you create a variable outside a function, the variable is global but if created inside a function, it is local.
# """The global Keyword(To create a global variable inside a function, you can use the global keyword.)"""
# # def myfunc():
# #   global x
# #   x = "fantastic"

# # myfunc()

# # print("Python is " + x)
# """To change the value of a global variable inside a function, refer to the variable by using the global keyword:"""
# # x = "awesome"

# # def myfunc():
# #   global x
# #   x = "fantastic"

# # myfunc()

# # print("Python is " + x)
# """Built-in Data Types
# ext Type:	str(Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.)
# Numeric Types:	int, float, complex(You cannot convert complex numbers into another number type.)
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType"""

# """Random Number: Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers"""
# """Python Casting: Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types."""

# #Check if "expensive" is NOT present in the following text:

# txt = "The best things in life are free!"
# if 'expensive' in txt:
#     print("'expensive' in txt")

# #Check if "expensive" is NOT present in the following text:
# txt = "The best things in life are free!"
# if 'expensive' not in txt:
#     print("'expensive' not in txt")

# """Remove Whitespace(The strip() method removes any whitespace from the beginning or the end:

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!")"""
# """Replace String(The replace() method replaces a string with another string:

# a = "Hello, World!"
# print(a.replace("H", "J")))"""
# """Split String(The split() method returns a list where the text between the specified separator becomes the list items.)The split() method splits the string into substrings if it finds instances of the separator:

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']"""

# """Python - Escape Characters(To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes)"""

# #to check if an item is present in a list
# thislist = ['apple', 'banana', 'cherry']
# if 'orange' in thislist:
#     print("yes, 'apple' is in this list")
# else:
#     print('none existing in this list')

# #change item of a list
#     lists = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#     lists[1:3] = ["blackcurrant", "watermelon"]
#     print(lists)

# #loop through a list
# list = ['apple', 'banana', 'cherry']
# for fruit in  list:
#     print(fruit)
# for fruit in range (len(list)):
#     print(fruit)

# #while loop
# mlist = ['apple', 'banana', 'cherry']
# i = 0
# while i < len(mlist):
#     print(mlist[1])
#     i = i+1

# #list comprehension(A short hand for loop that will print all items in a list)
# lst = ['apple', 'mango', 'pear']
# [print(x) for x in lst]
    
# fruit = ['cherry', 'tomato', 'apple', 'banana', 'kiwi', 'orange']
# newlist = []

# for x in fruit:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
# # or using list comprehension
# fruit = ['cherry', 'tomato', 'apple', 'banana', 'kiwi', 'orange']
# newlist = [x for x in fruit if 'a' in x]
# print(newlist)

# #customize sort function(The function will return a number that will be used to sort the list (the lowest number first)
# def myfunc(n):
#     return abs(n-50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# #using .append to concatinate two lists
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

#     print(list1)

# #or using extend()
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# #Tuples are used to store multiple items in a single variable
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# #to create a tuple of just one item(a tuple can contain different data types)
# tup = ("apple",)
# print(type(tup))

# #not a tuple
# tupl = ("apple")
# print(type(tupl))

# #to determine if a specific item is in a tuple
# thist = ('apple', 'banana', 'cherry')
# if "apple" in thist:
#     print("yes, 'apple' is in the fruits tuple")

# #tuples are unchangable and immutable bt cn be converted to a list and back to a tuple
# x = ('apple', 'banana', 'cherry')
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(y)
# print(x)

# #using * (If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list)
# fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruit
# print(green)    
# print(yellow)
# print(red)
# print(fruit)

# #python sets(True and 1 is considered the same value,The values False and 0 are considered the same value in sets, and are treated as duplicates)
# myset = {'apple','banana','cherry'}
# print(type(myset)) #set are used to store multiple items in a single variable
# print(myset)

# diset = {0, 'egg', 'dog', 'pig', True, 2, 1, False} #a set can be of any data type
# print(diset)

# #the double round bracket cab be used to create a set
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# #dictionaries(Dictionaries are used to store data values in key:value pairs.)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# #to get the value of the "model" key
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

# #creating a fxn
# def myfxn ():
#     print("Hello world")

# #calling a fxn
# def fxn():
#     print("hello world")
# fxn()

# #arguement
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# #arbitrary arguement(Arbitrary Arguments are often shortened to *args in Python documentations.)
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")
# #keyword arguement(The phrase Keyword Arguments are often shortened to kwargs in Python documentations(f you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition))
# #This way the function will receive a dictionary of arguments, and can access the items accordingly
# def my_functions(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_functions(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# #default parameter value(if we call the fxn without arg, it uses the default value)
# def my_func(country = 'Norway'):
#     print("I am from " + country)

# my_func('sweden')
# my_func('India')
# my_func('Brazil')
# my_func()

# #passing a list as an arguement
# def lst(fruits):
#     for x in fruits:
#         print(x)

# fruits = ["apple", "banana", "orange"]
# lst(fruits)

# #to let a fxn return a value
# def ret(x):
#     return(5*x)

# print(ret(3))
# print(ret(5))
# print(ret(9))

# #to combine positional arg with keyword arg
# #Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
# def my(a,b,/,*,c,d):
#     print(a+b+c+d)
# my(5,6, c=7, d=8)

# #recursion(a defined function can call itself.)
# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k-1)
#     else:
#         result = 0
#         return result
    
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# #python lambda(it is a small anonymous fxn, can take any number of arguements but only one expression)
# #lambda arguments : expression(The expression is executed and the result is returned)
# #Add 10 to argument a, and return the result:

# x = lambda a : a + 10
# print(x(5))

# # Multiply argument a with argument b and return the result:

# x = lambda a, b : a * b
# print(x(5, 6))

#using lambda with a user defined fxn
def myfc(n):
    return lambda a: a*n
mydoubler = myfc(2)
print(mydoubler(11))
mytriple = myfc(3)
print(mytriple(11))











