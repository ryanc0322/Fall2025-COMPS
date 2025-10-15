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

def format_money(x):
    return f"${x:,.2f}"

def choose_item(items, categories, prices):
    idx = random.randrange(len(items))
    return {
        "name": items[idx],
        "category": categories[idx],
        "base_price": prices[idx],
        "quality": random.choice(QUALITY),
    }


'''
Part 1: User Inputs
'''
# TODO: Make function to prompt users for name and balance
def get_user_info():

# TODO: Make function to prompt users for yes and no
def prompt_yes_no(prompt):

# TODO: Make function to prompt users for a float
def prompt_float(prompt, allow_zero=False):

def prompt_end_shopping():

'''
Part 2: Adding Purchases
'''

def calculate_surcharge(active_plans):
    return sum(p['install'] for p in active_plans if p['remaining'] > 0)

# TODO: Function that displays the items
def display_offer(item, surcharge, total):

# TODO: Function that applies the purchase to the balance as well as the active payment plans
def apply_purchase(balance, total_price, active_plans):

# TODO: Function to create a payment plan
def create_payment_plan_if_offered(item_name, base_price, active_plans):

# TODO: Function that prompts users to add a deposit to their account after a purchase
def post_purchase_deposit(balance):

# TODO: Function that prompts users to deposit money into their account if their balance drops below 0 or cancel the prucahse otherwise
def ensure_funds(balance, total_price):



'''
Part 3: Creating the Simulator
'''

# TODO: Put everything we've worked on together in main

def main():



