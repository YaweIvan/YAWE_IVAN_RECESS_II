# Step 1: Initial stock in a small grocery store
#inventory = {"item": quantity} dict
inventory = {
    "Sugar": 25,
    "Rice": 40,
    "Cooking Oil": 15,
    "Bread (loaves)": 20
}

# Step 2: Keep the program running until the user chooses to exit
while True:
    print("\nGROCERY STORE INVENTORY SYSTEM")
    print("1. View Current Stock")
    print("2. Restock Item / Add New Item")
    print("3. Sell Item")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Step 3: View inventory
    if choice == "1":
        print("\nCurrent Stock")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} units")

    # Step 4: Add or update stock
    elif choice == "2":
        item_name = input("Enter the name of the item to restock: ")
        quantity = int(input("Enter quantity to add: "))
       
        if item_name in inventory:
            inventory[item_name] += quantity
            print(f"Restocked {item_name}. New quantity: {inventory[item_name]} units.")
        else:
            inventory[item_name] = quantity
            print(f"Added new item: {item_name} with {quantity} units.")

    # Step 5: Sell item (reduce quantity)
    elif choice == "3":
        item_name = input("Enter the item sold: ")
        if item_name in inventory:
            try:
                quantity_sold = int(input(f"Enter quantity sold of {item_name}: "))
            except ValueError:
                print("Please enter a valid number for quantity.")
                continue

            if quantity_sold <= inventory[item_name]:
                inventory[item_name] -= quantity_sold
                print(f"Sold {quantity_sold} units of {item_name}. Remaining: {inventory[item_name]}")
            else:
                print("Not enough stock to complete the sale.")
        else:
            print("Item not found in inventory.")

    # Step 6: Exit the program
    elif choice == "4":
        print("Exiting system. Thank you!")
        break

    # Step 7: Invalid option
    else:
        print("Invalid option. Please choose between 1 and 4.")
