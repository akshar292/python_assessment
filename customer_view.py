

import data_manager
import utils
import logging

def view_available_fruits(stock):
    
    print("\n--- AVAILABLE FRUITS ---")
    if not stock:
        print("Sorry, the market is currently out of stock.")
        return False
    
    print("Fruits available for purchase:")
    for fruit, details in stock.items():
        if details.get('qty', 0) > 0:
            print(f"- {fruit}: ${details['price']:.2f}/kg")
    return True

def purchase_fruit(stock):
   
    print("\n--- PURCHASE FRUIT ---")
    if not view_available_fruits(stock):
        return

    fruit_name = input("Enter the name of the fruit you want to buy: ").strip().title()

    if fruit_name not in stock or stock[fruit_name]['qty'] <= 0:
        print(f"Sorry, '{fruit_name}' is not available.")
        return

    available_qty = stock[fruit_name]['qty']
    print(f"There are {available_qty} kg of {fruit_name} available.")
    
    qty_to_buy = utils.get_validated_numeric_input(f"Enter quantity of {fruit_name} to buy (in kg): ", float)

    if qty_to_buy <= 0:
        print("Error: Quantity must be positive.")
        return
    if qty_to_buy > available_qty:
        print(f"Error: Not enough stock. Only {available_qty} kg available.")
        return

    price = stock[fruit_name]['price']
    total_cost = qty_to_buy * price

    print(f"\nYou are purchasing {qty_to_buy} kg of {fruit_name} for a total of ${total_cost:.2f}.")
    confirm = input("Confirm purchase? (y/n): ").lower()

    if confirm == 'y':
        stock[fruit_name]['qty'] -= qty_to_buy
        data_manager.save_stock(stock)
        logging.info(f"Customer purchase: {qty_to_buy} kg of {fruit_name} for ${total_cost:.2f}")
        print("Thank you for your purchase!")
    else:
        print("Purchase cancelled.")

def run_customer_view():
   
    stock = data_manager.load_stock()

    while True:
        print("\n--- Welcome, Customer! ---")
        print("1) View Available Fruits")
        print("2) Purchase Fruit")
        print("3) Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_available_fruits(stock)
        elif choice == '2':
            purchase_fruit(stock)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")