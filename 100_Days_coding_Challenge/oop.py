
# class Car:

#     #attribute, properties.
#     #class attribute(every object can inherit it)
#     state = "flying_car"
#     color = "silver"
#     tyre = "six-tyres"
#     mode_of_movement = "water"

# # constructor method(creating an object outside of a class)
#     def__init__(self) -> None:#called a magic metd abd it wont return anything
#         pass
#     #instance attribute.
#     Car.color = "blue"
#     mercedis = Car()
#     print(mercedis.state)
#     print(mercedis.color)
#     print(mercedis.tyre)
#     print(mercedis.mode_of_movement)

# Class creation and object instantiation from the class created and how class attribute and instance attribute can be determined and the difference including the proocess of instantiation
#creating a class that will be used to build a pen
# to create a class in python, one has to start with the keyword class and the name must begin with a capital letter

class Cristal:
    #pass no error, just passover the empty class crystal
    color = "Blue" #an attribute is simply creating a variable in classes
#method:a function used in a class (the behaviour of the object)
def write (self): #a user defined function,self(an object you are yet to create)
    print("Hey! I am writing")
#to use a method, there must be a an object and this object is an instance of the class(an object created from a class)
#a placeholder must be passed in def write (----)
#Instantiation(creating an instance of the class => object)
first_pen = Cristal()
first_pen.write()#if we want first pen to write, we add . and the name of the function write
