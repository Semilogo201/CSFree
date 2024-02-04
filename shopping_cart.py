cart = []

while True:
    print("1. Add item to cart")
    print("2. View Cart")
    print("3. Calculate total cost")
    print("4. Exit")
    try:
       choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number. ")
        continue
    
    if choice == 1:
        item_name = input("Enter the item price: ")
        item_price = float(input("Enter the item price: "))
        cart.append({'name': item_name, 'price': item_price})
        print(f"{item_name} added to the cart. ")

    elif choice == 2:
        for i, item in enumerate(cart):
            print(f"{i + 1}, {item['name']} - ${item['price']}")
        
    elif choice == 3:
        total_cost = sum(item['price'] for item in cart)
        print(f"Total Cost: $(total_cost)")

    elif choice == 4:
        print("Exit the shopping cart program")
        break
    print("what else would you like to do")
else:
        print("What else would you like to do?")