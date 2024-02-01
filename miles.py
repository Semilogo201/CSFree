while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == 'quit':
        print("Exiting the program")
        break
    #isdigit helps it not to take any other thing asides integer
    elif user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
else:
    print("Invalid input. Please enter a number or 'quit' ")

user_input = int(input("Enter a non-negative number: \n"))
 