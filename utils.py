import logging

LOG_FILE = 'transactions.log'

def setup_logging():
    
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_validated_numeric_input(prompt, num_type=float):
 
    while True:
        try:
            value = num_type(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:

            print(f"Invalid input. Please enter a valid number.")
