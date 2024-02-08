# The best when working with optional arg is to use the keyword arguement. Basically, I know how to create, call, pass parameters,pass arg to a function and use the output of a function.
#function declaration
#To make a parameter optional, you need to create a default parameter or default value for the parameter
# def greeting(fname, lname, mname=None, title="Mr/Mrs/Miss"): #function parameters
#  o   if mname is not None:
#         str_to_return = f"Hi {title}, your full name is {fname} {mname} {lname}"
#     else:
#         str_to_return = f"Hi {title}, your full name is {fname} {lname}"
#     return str_to_return
# #calling the function(using the keyword arg, if one uses positional arg, the optional arg must be the last arg )
# milo = greeting(fname="Oluwasemilogo",lname="Adeyemi",mname="Oluwaseun",title="Engr")#parameters taking in arguements
# milo = greeting(fname="Oluwasemilogo",lname="Adeyemi")
# #greeting("Kelly" "Mistar")
# #greeting("Julien", "Sir")
# print(milo)

#To create fxns that takes in a wide range of data, we use the varadic fxn(it takes in variable numbers of arguement). It can be done using data structures(list,tuples,dictionaries and set)
def greet_user (*name): #*name = a tuple.function parameter
    print(name)
greet_user("milo") #the fxn has received an arguement and it can still take in a lot more by inserting *.
greet_user("milo", "Dami", "tobi", "yusuf", "benji", "emma", "raf")

def greet_user(**args):
    #args => a tuple(with just one *)
    # **kwargs => dictionary (with two **)(a dict always have a key and a value)
    print(kwargs)

    #greet_user("milo")
    {"fname" : "Oluwasemilogo", "lname" : "adeyemi"}#this is a dictionary
    greet_user("milo", "adeyemi", "29")
#Anonymous functions(lambda function)when looking for a modular code you are not looking for reusability.
def sum(x,y):
    return x+y
v = sum(2,3)
print(v)