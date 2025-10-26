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

def read_items(filename):
    """
    Reads product information from a CSV file.

    Parameters:
    filename (str): The path to the CSV file.
    
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

    # TODO: Implement function
    pass

def apply_purchase(balance, total):
    """
    Subtracts the cost of a purchase from the user's balance

    Parameters:
    balance (float): current balance
    total (float): cost of the purchase, plus any payment plan fees

    Returns:
    new_balance (float): the updated balance
    """

    # TODO: Implement function
    pass

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
    # TODO: Implement function
    pass

def apply_payment_plans(balance, payment_plans):
    """
    Applies all active payment plans to the shoppers's balance.

    Parameters:
    balance (float): Current balance.
    payment_plans (list of dict): Active payment plans.

    Returns:
    tuple:
        - balance (float): Updated balance
        - updated_plans (list of dict): Payment plans with decremented 'num_payments' and finished plans removed.
    """
    # TODO: Implement function
    pass

def discount(price):
    """
    Randomly applies a 5-15% discount 50% of the time.

    Parameters:
    price (float): Original price of the product.

    Returns:
    tuple:
        - final_price (float): The price after any discount.
        - discount_flag (int): 1 if a discount was applied, 0 otherwise.
    """
    # TODO: Implement function
    pass

def simulation():
    """
    Runs the shopping simulation.

    Steps:
    1. Greets the user and gets their name and initial balance.
    2. Loads product data from 'products.csv'.
    3. Enters a loop where:
        a. If balance is zero or negative, exits the loop.
        b. Applies  active payment plans to the balance.
        c. Offers a random product to the shopper.
        d. Applies a discount at random to the product price.
        e. Displays product details and current balance.
        f. Prompts the shopper to buy, see another product, or exit.
        g. If buying and price > $35, offers to create a payment plan.
        h. Updates balance and payment plans based on shopper actions.
        i. User continues shopping until they choose to exit or run out of funds.
    4. Thanks the user and displays their final balance upon exit.
    """

    print("------------------- Welcome to the Shopping Simulator! -------------------")

    # Shopper info, data loading, and initialize payment plans
    name = input("What's your name? ").strip()
    while True:
        balance_input = input("Enter your current balance: ").strip()
        try:
            balance = float(balance_input)
            if balance < 0:
                print("Invalid input. Balance can't be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Balance must be a number.")

    products, categories, prices = read_items("products.csv")
    payment_plans = []

    while True:

        # Check if balance is zero
        if balance <= 0:
            print("You have no money left! Please come back with more funds.")
            break

        # Apply active payment plans using the apply_payment_plans function
        if payment_plans:
            balance, payment_plans = apply_payment_plans(balance, payment_plans)
            total_payments_left = 0
            for plan in payment_plans:
                total_payments_left += plan['num_payments']
            # Print payment plan summary
            print(f"\n--- Payment Plans Applied ---")
            print(f"Remaining active plans: {len(payment_plans)}")
            print(f"Total payments left: {total_payments_left}")
            print(f"New balance: ${balance:.2f}")
            print("-----------------------------\n")

        # Offer a product using the offer_product function
        product = offer_product(products, categories, prices)
        # Apply discount using the discount function
        final_price, discount_flag = discount(product['price'])
        # Display product details
        print(f"--------------------------- Product Offer ---------------------------")
        print(f"Offer: {product['name']} in {product['category']}")
        if discount_flag:
            print(f"DISCOUNT APPLIED! Original price: ${product['price']:.2f} -> Discounted price: ${final_price:.2f}")
        else:
            print(f"Price: ${final_price:.2f}")

        print(f"Your current balance: ${balance:.2f}")

        # Prompt shopper to buy, see another product, or exit
        while True:
            choice = input("Would you like to buy? (yes/no): ").strip().lower()
            if choice in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if choice == "yes":
            # Offer payment plan if price > $35
            if final_price > 35:
                while True:
                    plan_choice = input("This item qualifies for a payment plan! Set one up? (yes/no): ").strip().lower()
                    if plan_choice in ["yes", "no"]:
                        break
                    print("Please enter 'yes' or 'no'.")
                if plan_choice == "yes":
                    # Create payment plan using the create_payment_plan function
                    payment_plans = create_payment_plan(payment_plans, final_price)
                    plan = payment_plans[-1]
                    # Apply first payment using the apply_purchase function
                    balance = apply_purchase(balance, plan["payment_amount"])
                    print(f"Payment plan created: 3 payments of ${plan['payment_amount']:.2f}")
                else:
                    if balance >= final_price:
                        # Apply purchase using the apply_purchase function
                        balance = apply_purchase(balance, final_price)
                        print(f"Purchased {product['name']} for ${final_price:.2f}")
                    else:
                        print("Your balance is too low. Please come back with more funds.")
                        break
            else:
                if balance >= final_price:
                    # Apply purchase using the apply_purchase function
                    balance = apply_purchase(balance, final_price)
                    print(f"Purchased {product['name']} for ${final_price:.2f}")
                else:
                    print("Your balance is too low. Please come back with more funds.")
                    break

        elif choice == "no":
            while True:
                next_choice = input("Would you like to see a different product? (yes/no): ").strip().lower()
                if next_choice in ["yes", "no"]:
                    break
                print("Please enter 'yes' or 'no'.")
            if next_choice == "no":
                print(f"\nThank you for shopping, {name}! Final balance: ${balance:.2f}")
                break


def main():
    simulation()


if __name__ == "__main__":
    main()
