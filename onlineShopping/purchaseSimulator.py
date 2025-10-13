'''
purcahseSimulator.py

Jamal Omosun

Description:
'''
import random
import csv
import sys

QUALITY = ["poor", "mediocre", "good", "excellent"]

filename = "purchaseItems.csv"

def read_items(filename):
    items = []
    categories = []
    prices = []
    try:
        with open(filename, newline='') as fh:
            reader = csv.reader(fh)
            headers = next(reader, None)
            for row in reader:
                if len(row) < 3:
                    continue
                categories.append(row[0].strip())
                items.append(row[1].strip())
                try:
                    prices.append(float(row[2]))
                except ValueError:
                    prices.append(0.0)
    except FileNotFoundError:
        print(f"Could not find {filename}. Exiting.")
        sys.exit(1)
    return items, categories, prices

# TODO: Print the first row 

# TODO: Print the items, prices and categories

'''
Part 2: User Inputs
'''

# TODO: Make function to prompt users for yes and no

# TODO: Make function to prompt users for a float

'''
Part 3: Creating the Simulator
'''

# TODO: Prompt user for name and current balance

# TODO: Purchase items and subtract from balance

# TODO: Prompt users to add funds to balance

# TODO: End program when user balance goes below 0 and they don't deposit

# TODO : Add purchase plan for items > $35



