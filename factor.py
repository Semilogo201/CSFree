#Write a Python program that takes a number as input from the user and prints the factorial of that number. Use a while loop to validate that the input is a non-negative integer, and then use a for loop to calculate the factorial.
def factorial(number):
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i
    return factorial_result  


while True:
    user_input = input("Enter a positive number: \n")

    if user_input.lstrip("-").isdigit():
        number = int(user_input)
        if number >= 0:
            answer = factorial(number)
            print(f"the factorial of {number} is {answer}")
            break
        else:
            print("please enter a non-negative integer. \n")

    else:
        print("please enter an integer.")