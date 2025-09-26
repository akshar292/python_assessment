

import manager_view
import customer_view
import utils

def main():
   
    utils.setup_logging()
    
    while True:
        print("\n" + "="*20)
        print("WELCOME TO FRUIT MARKET")
        print("="*20)
        print("1) Manager")
        print("2) Customer")
        print("3) Exit")
        
        role_choice = input("Select your Role: ")

        if role_choice == '1':
            manager_view.run_manager_view()
        elif role_choice == '2':
            customer_view.run_customer_view()
        elif role_choice == '3':
            print("Thank you for using the Fruit Market Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid role (1, 2, or 3).")

if __name__ == "__main__":
    main()