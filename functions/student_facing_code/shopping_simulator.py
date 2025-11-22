"""
shopping_simulator.py

Jamal Omosun and Chloe Simanek

Description: This program includes several functions that are used in an
online shopping simulator. The functions handle product offers, payment plans,
discounts and purchases. Use run_simulator.py to run the full simulation.
"""
# TODO: fix docstrings 

import random
import csv
import sys

# ! DO NOT MODIFY THIS FUNCTION !
def read_items(filename):
    """Reads product information from a CSV file.

    Args:
        filename (str): Path to CSV file.
    
    Returns:
        tuple: Three lists containing product names, categories, and prices. 
    """
    products = []
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
                products.append(row[1].strip())
                try:
                    prices.append(float(row[2]))
                except ValueError:
                    prices.append(0.0)
    except FileNotFoundError:
        print(f"Could not find {filename}. Exiting.")
        sys.exit(1)
    return products, categories, prices

def apply_purchase(balance, total):
    """Subtract cost from balance.

    Args:
        balance (float): The current balance.
        cost (float): Cost of a purchase.

    Returns:
        new_balance (float): The updated balance. 
    """

    # TODO: Implement function
    pass

def offer_product(products, categories, prices):
    """Offer a random product from the available products. 

    Args:
        products (list): Product names.
        categories (list): Product categories.
        prices (list): Product prices.

    Returns:
        dict: A dictionary with keys "name", "category", and "price". 
    """

    # TODO: Implement function
    pass

def create_payment_plan(payment_plans, product_price):
    """Create and add a new payment plan to the list.

    The plan includes a 10% surcharge on the product price and divides 
    the total cost into three equal payments.

    Args:
        payment_plans (list[dict]): Existing payment plans. 
            Each plan should contain:
                - 'num_payments' (int): Number of payments.
                - 'payment_amount' (float): Dollar amount per payment.
        product_price (float): Price of the product to create a plan for.

    Returns:
        payment_plans (list of dict): Updated list of payment plans,
            including the new plan.
    """
    # TODO: Implement function
    pass

def apply_payment_plans(balance, payment_plans):
    """Apply all active payment plans to the shoppers's balance.

    For each active payment plan, meaning there are still payments
    remaining (num_payments > 0). Deduct one payment from the balance and 
    decrement the number of payments. Completed plans (num_payments = 0)
    are removed.

    Args:
        balance (float): Shopper's current balance.
        payment_plans (list[dict]): Active payment plans.
            Each plan should contain:
                - 'num_payments' (int): Number of payments.
                - 'payment_amount' (float): Dollar amount per payment.

    Returns:
        tuple:
            balance (float): Updated balance after applying all payments.
            updated_plans (list[dict]): Updated list of active payment plans
                with decremented 'num_payments' and completed plans removed.
    """
    # TODO: Implement function
    pass

def discount(price):
    """Randomly apply a 5-15% discount 50% of the time.

    Args:
        price (float): Original price of the product.

    Returns:
        tuple:
            - final_price (float): Price after a discount.
            - discount_flag (int): 1 if a discount is applied, otherwise 0.
    """
    # TODO: Implement function
    pass
