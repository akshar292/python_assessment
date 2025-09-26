
import json

STOCK_FILE = 'stock.json'

def load_stock():
   
    try:
        with open(STOCK_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_stock(stock_data):
   
    with open(STOCK_FILE, 'w') as f:
        json.dump(stock_data, f, indent=4)