balance = 0
print("welcome to your budget tracker")

while True:
    print("1. Add income: ")
    print("2. Add expenses")
    print("3. current balance")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number: ")
    if choice == 1:
        income_amount = float(input("Enter your income"))
        balance += income_amount
        print(f"income of $ {income_amount} added. updated balance: ${balance}")
    elif choice == 2:
        expense_amount = float(input("Enter your expenses"))
        balance -= expense_amount
        print(f"expense of $ {expense_amount} deducted. ")
    elif choice == 3:
        print(f"current_balance of $ {balance}")
    elif choice == 4:
        print("Exit the budget tracker program")
        break
    else:
        print("Invalid choice, Please enter a number between 1 and 4")