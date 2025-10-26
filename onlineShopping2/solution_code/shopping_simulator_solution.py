"""
shopping_simulator_solution.py

Jamal Omosun and Chloe Simanek

Description: Student solution for shopping simulator functions.
Use run_simulator.py to run the full simulation.
"""

import random
import csv
import sys

# ! DO NOT MODIFY THIS FUNCTION !
def read_items(filename): # pragma: no cover
    """Reads product information from a CSV file.

    Args:
        filename (str): Path to CSV file
    
    Returns:
        tuple: Three lists containing product names, categories, and prices.
    """
    products = []
    categories = []
    prices = []
    try:
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) < 3:
                    continue
                categories.append(row[0].strip())
                products.append(row[1].strip())
                try:
                    prices.append(float(row[2]))
                except ValueError:
                    prices.append(0.0)
    except FileNotFoundError:
        print(f"Could not find {filename}. Exiting.")
        sys.exit(1)
    return products, categories, prices


def offer_product(products, categories, prices):
    """
    Offers a random product from the available items

    Parameters:
    products (list): List of product names
    categories (list): List of product categories
    prices (list): List of product prices

    Returns:
    dict: A dictionary with keys "name", "category", and "price"

    """
    idx = random.randrange(len(products))
    return {
        "name": products[idx],
        "category": categories[idx],
        "price": prices[idx]
    }

def apply_purchase(balance, cost):
    """
    Subtracts the cost of a purchase from the user's balance

    Parameters:
    balance (float): current balance
    cost (float): cost of the purchase

    Returns:
    new_balance (float): the updated balance
    """
    newBalance = balance - cost
    return newBalance

def create_payment_plan(payment_plans, product_price):
    """
    Creates a payment plan with the following characteristics:
        - 10% surcharge on the product price
        - 3 equal payments
    
    Parameters:
    payment_plans (list of dict): Existing active payment plans.
        Each dictionary contains:
            - 'num_payments' (int): Payments remaining.
            - 'payment_amount' (float): Amount per payment.
    product_price (float): Price of the product to create a plan for.

    Returns:
    payment plans (list of dict): Updated list of payment plans including the new plan.
    """
    num_payments = 3
    surcharge = product_price * 0.10
    payment_amount = (product_price + surcharge) / num_payments
    new_plan = {"num_payments": num_payments, "payment_amount": payment_amount}
    payment_plans.append(new_plan)
    return payment_plans

def apply_payment_plans(balance, payment_plans):
    """
    Applies all active payment plans to the shoppers's balance.

    Parameters:
    balance (float): Current balance.
    payment_plans (list of dict): Active payment plans.

    Returns:
    tuple:
        - balance (float): Updated balance
        - updated_plans (list of dict): Payment plans with decremented
          'num_payments' and finished plans removed.
    """
    total_payment = 0
    for plan in payment_plans:
        total_payment += plan["payment_amount"]
    balance = apply_purchase(balance, total_payment)

    updated_plans = []
    for p in payment_plans:
        p["num_payments"] -= 1
        if p["num_payments"] > 0:
            updated_plans.append(p)

    return balance, updated_plans

def apply_discount(price):
    """
    Randomly applies a 5-15% discount 50% of the time.

    Parameters:
    price (float): Original price of the product.

    Returns:
    tuple:
        - final_price (float): The price after any discount.
        - discount_flag (int): 1 if a discount was applied, 0 otherwise.
    """
    discount_flag = 0
    final_price = price
    if random.choice([True, False]):
        percent = random.randint(5, 15) / 100
        final_price = round(price * (1 - percent), 2)
        discount_flag = 1
    return final_price, discount_flag
