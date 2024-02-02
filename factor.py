#Write a Python program that takes a number as input from the user and prints the factorial of that number. Use a while loop to validate that the input is a non-negative integer, and then use a for loop to calculate the factorial.
def factorial(number): #defining a factorial number
    factorial_result = 1 #whateva you have should start from one
    for i in range(1, number + 1): #whatever input will start from 1 and will count to the actual number
        factorial_result *= i 
    return factorial_result  


while True:
    user_input = input("Enter a positive number: \n")

    if user_input.lstrip("-").isdigit():#LSTRIP WILL CHECK IF YOU PUT A -VE SIGN
        number = int(user_input)
        if number >= 0:
            answer = factorial(number)
            print(f"the factorial of {number} is {answer}")
            break
        else:
            print("please enter a non-negative integer. \n")

    else:
        print("please enter an integer.")