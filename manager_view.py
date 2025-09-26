

import data_manager
import utils
import logging

def add_fruit_stock(stock):
    
    print("\n--- ADD FRUIT STOCK ---")
    fruit_name = input("Enter fruit Name: ").strip().title()
    
    if fruit_name in stock:
        print(f"Error: Fruit '{fruit_name}' already exists. Use the update option instead.")
        return

    qty = utils.get_validated_numeric_input("Enter qty (in kg): ", float)
    price = utils.get_validated_numeric_input("Enter price (for kg): ", float)
    
    stock[fruit_name] = {'qty': qty, 'price': price}
    data_manager.save_stock(stock)
    logging.info(f"Stock added: {fruit_name}, Qty: {qty} kg, Price: ${price:.2f}/kg")
    print(f"Success: Stock for '{fruit_name}' added successfully.")

def view_fruit_stock(stock):
    
    print("\n--- VIEW FRUIT STOCK ---")
    if not stock:
        print("The fruit stock is currently empty.")
    else:
        print("Current Stock:")
        for fruit, details in stock.items():
            print(f"- {fruit}: Qty: {details['qty']} kg, Price: ${details['price']:.2f}/kg")

def update_fruit_stock(stock):
    
    print("\n--- UPDATE FRUIT STOCK ---")
    fruit_name = input("Enter the name of the fruit to update: ").strip().title()

    if fruit_name not in stock:
        print(f"Error: Fruit '{fruit_name}' not found in stock.")
        return

    print(f"Updating '{fruit_name}'. Current details: {stock[fruit_name]}")
    update_choice = input("Update price (p), quantity (q), or both (b)? ").lower()

    if 'p' in update_choice or 'b' in update_choice:
        new_price = utils.get_validated_numeric_input("Enter new price: ", float)
        stock[fruit_name]['price'] = new_price
        logging.info(f"Stock price updated for {fruit_name} to ${new_price:.2f}/kg")

    if 'q' in update_choice or 'b' in update_choice:
        new_qty = utils.get_validated_numeric_input("Enter new quantity: ", float)
        stock[fruit_name]['qty'] = new_qty
        logging.info(f"Stock quantity updated for {fruit_name} to {new_qty} kg")

    data_manager.save_stock(stock)
    print(f"Success: Stock for '{fruit_name}' updated successfully.")

def run_manager_view():
    
    stock = data_manager.load_stock()
    
    while True:
        print("\n--- Fruit Market Manager ---")
        print("1) Add Fruit Stock")
        print("2) View Fruit Stock")
        print("3) Update Fruit stock")
        print("4) Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_fruit_stock(stock)
        elif choice == '2':
            view_fruit_stock(stock)
        elif choice == '3':
            update_fruit_stock(stock)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")