"""we have ways of handling  errors in python in regards to what the end user is going to input
built-in rrrors:in python 
user-defined errors(custom errors):you built yourself
the master of all errors is referred to as base-exceptions and you dont want to tamper with it because it can crash ones work.
exceptions are run-time errors 
sub class of base exception is the master exception(arithmetic exception(floating point, zero division, overflow), assertion error, attribute error,buffer error, eof error, input error, module not found error )
types of possibe errors we can experience
Note: errors potentially crash programs.
Error Handling and we have two keyword
#catching exceptions:errors at run time (try-it consist of your line of code(the user didnt use it the way they were suppose to) and except- it helps defend your total program from crashing(it can invoke the error present in the program), we use it to catch the error and terminate it), we also have else, finally and raise are used to catch errors.
#Raising exceptions"""

# try:
#     numerator = int(input("Enter a numerator: "))
#     denominator =int(input("Enter the denominator: "))
#     divisionResult = numerator/denominator
#     print(f"Result: {divisionResult}") 
# except ZeroDivisionError:
#     print("Error, cannot divide by 0")
# except ValueError: #whatever it is printing out, save it as value
#     print("Error, an integer expected not a string")

# while True: #without any break statement, it will continue to prompt the prog except we use ctrl+d(eof error) and the error can be handled 
#     try:
#         numerator = int(input("Enter a numerator: "))
#         denominator =int(input("Enter the denominator: "))
#         divisionResult = numerator/denominator
#         print(f"Result: {divisionResult}") 
#     except ZeroDivisionError:
#         print("Error, cannot divide by 0")
#     except ValueError: #whatever it is printing out, save it as value
#         print("Error, an integer expected not a string")
#     except EOFError:
#         print("ctrl d entered") 
#     else:
#         print("An error was not encountered") #if no error was encountered, else will be executed
#     finally:
#         print("End of program") #it will always be executed if an error was found or not

# """Raising exceptions is you explicitly trying to invoke an error or call an error, you are trying to wake the sleeping error
# you raise an error when you are so sure of the type of error in question
# you can raise errors through if/else and using try and except too"""
# raise SyntaxError("I raised SyntaxError") # you are manually calling the error

def positive(value): 
    try:
        if value < 0: #raise eexception type("Error message")
         raise ValueError("Enter a positive value")
    except ValueError:
        print("Enter a positive value")
    finally:
       print(value)
positive(-8)
#note: when you raise an error, it crashes the program. the code has the potential to crash at line 50 because that is where the function is called.