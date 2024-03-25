
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
# creating a class that will be used to build a pen
# to create a class in python, one has to start with the keyword class and the name must begin with a capital letter

# class Cristal:
#     #pass no error, just passover the empty class crystal
#     color = "Blue" #an attribute is simply creating a variable in classes
#     def __init__(self, id): #magic metd(donda metd have double -- before and after) id here is the attribute itself
#         self.id = id #id equals the self id of each objects we are going to create
#         print("You just created an object")
#     #method:a function used in a class (the behaviour of the object)
# def write(self): #a user defined function,self(an object you are yet to create)
#     print("Hey! I am writing") #26-31 is just a template,it won't output anything to the console
# #to use a method, there must be a an object and this object is an instance of the class(an object created from a class)
# #a placeholder must be passed in def write (----)
# #Instantiation(creating an instance of the class => object)
# first_pen = Cristal(id="sl-01")
# #if we want first pen to write, we add . and the name of the function write
# first_pen.write()
# #to access the attribute
# print(f"Color of first pen is {first_pen.color}")
# print(f"id of first pen is {first_pen.id}")

# #creating another instance of our class
# second_pen = Cristal(id="sl-02")
# print(f"Color of second pen is {second_pen.color}")
# # print(f"id of second pen is {second_pen.id}")

# #oop class(we have created our own data type just like we can have inbuilt data types)
# class Instructor: #we have created the class called instructor
#     def __init__(self, instructor_name, address): #self indicates the actual object we are calling
#         self.ins_name=instructor_name #the attribute name can be anything, ins_name is just a variable name that holds the instructor_name
#         self.add=address #add is the variable name that holds the argument address
#         self.followers=0 #instead of making it a compulsory arguement, we will just define it under self  
#         # print("Creating a new object")
#     # pass #since our call has no () yet
# instructor_1 = Instructor("Yusuf", "Lagos") # we are defining the first object in our class Instructor
# instructor_2 = Instructor("Bello", "Egypt")
# print(type(instructor_1))
# print(instructor_1.ins_name)
# print(instructor_2.add)
# print(instructor_1.followers)
# # instructor_1.name = "Yusuf" #we cant write the name without adding .name because .name is now an attribute of the instructor
# # instructor_1.address = "Lagos state"
# # print(instructor_1.name)
# # print(instructor_1.address)

# # instructor_2.name = "Bello" #we cant write the name without adding .name because .name is now an attribute of the instructor
# # instructor_2.address = "Egypt"
# # print(instructor_2.name)
# # print(instructor_2.address) #if we have alot of instructors, doing it this way will be stressful. We make use of a constructor and the essence is for it to intialize data members of a class
# """The constructor will help us to know what will happen when we create the object. the constructor assigns values to thee data members of a class when an object is created. so we can introduce a simple function which is the def __init__(self) and it is a predifined method and it help to initialize the object and the init function will be called anytime you create an object
# after defining the attribute at the top, we dont need to write each instructor with their attribut. The attributes will be written in the self column where we used the predefined fxn init
# self is just a keyword to bind the actual object with the value
# """


