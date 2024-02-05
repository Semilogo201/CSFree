#A code that allows multiple withdrawal 
print("welcome")
print("Please enter your secret number")
secret_num = input("secret number: ")

while len(secret_num) != 4: #or not secret_num.isdigit():
      print("Invalid secret number. Please enter exactly 4 digits.")
      break     
while True: #entering a continous loop and presenting a menu to the user for the requested options
    
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Exit")
     
    try:
            options = int(input("Enter your option (1-3): "))
    except ValueError: 
            print("Invalid input. please enter a valid option: ")
            continue  
    if options == 1:
        withdrawal = float(input("Enter withdrawal amount:#"))
        print(f"Withdrawal amount is {withdrawal}")
    elif options == 2:
        Deposit = float(input("Amount you intend to deposit: "))
        print(f"Deposited amount is {Deposit}")
    elif options == 3:
        print("Exit")
    break
else:
    print("Invalid option. Please enter a number between 1-3")   
