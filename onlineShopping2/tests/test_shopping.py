import pytest
from shoppingSimulatorSol import *
import csv
import random

# ###########################################
# #          load data for testing          #
# ###########################################

products = []
categories = []
prices = []

with open("./products.csv", newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        products.append(row["Product Name"])
        categories.append(row["Category"])
        prices.append(float(row["Approximate Price (USD)"]))

# #########################################
# #          offer_product tests          #
# #########################################

def test_empty_functions():
    """
    Test that functions are implemented.
    """
    assert offer_product(products, categories, prices) is not None, "offer_product not implemented"
    assert apply_purchase(100.0, 50.0) is not None, "apply_purchase not implemented"
    assert create_payment_plan([], 200.0) is not None, "create_payment_plan not implemented"
    assert apply_payment_plans(300.0, []) is not None, "apply_payment_plans not implemented"
    assert discount(100.0) is not None, "discount not implemented"

def test_offer_product_keys():
    """
    Test that the dictionary returned by offer_product has the correct keys.
    """
    product = offer_product(products, categories, prices)
    assert "name" in product
    assert "category" in product
    assert "price" in product

def test_offer_product_valid_row():
    """
    Test that the offer_product function returns valid data from the CSV file.
    """
    product = offer_product(products, categories, prices)
    found = False
    for i in range(len(products)):
        if (products[i] == product["name"]
            and categories[i] == product["category"]
            and prices[i] == product["price"]):
            found = True
            break
    assert found, "Product not found in data."

def test_offer_product_randomness():
    """
    Test that offer_product returns random products. 
    """
    offer1 = offer_product(products, categories, prices)
    offer2 = offer_product(products, categories, prices)
    assert offer1 != offer2, "offer_product should return random products."


# ##########################################
# #          apply_purchase tests          #
# ##########################################


def test_apply_purchase():
    """
    Test that apply_purchase correctly calculates the balance.
    """
    balance = random.randint(100, 1000)
    cost = random.randint(100, 1000)
    new_balance = apply_purchase(balance, cost)
    assert new_balance == balance - cost, "apply_purchase did not correctly calculate the balance."

# ###############################################
# #          create_payment_plan tests          #
# ###############################################

# def create_payment_plan(payment_plans, product_price):
#     """
#     Creates a payment plan with the following characteristics:
#         - 10% surcharge on the product price
#         - 3 equal payments
    
#     Parameters:
#     payment_plans (list of dict): Existing active payment plans.
#         Each dictionary contains:
#             - 'num_payments' (int): Payments remaining.
#             - 'payment_amount' (float): Amount per payment.
#     product_price (float): Price of the product to create a plan for.

#     Returns:
#     payment plans (list of dict): Updated list of payment plans including the new plan.
#     """
#     # TODO: Implement function
#     num_payments = 3
#     surcharge = product_price * 0.10
#     payment_amount = (product_price + surcharge) / num_payments
#     new_plan = {"num_payments": num_payments, "payment_amount": payment_amount}
#     payment_plans.append(new_plan)
#     return payment_plans

def test_create_payment_plan_structure():
    """
    Test that create_payment_plan returns a list of dictionaries with num_payments and payment_amount.
    """
    payment_plans = []
    product_price = random.randint(100, 1000)
    # TODO 

def test_create_payment_plan_amount():
    """
    Test payment_amount calculated in create_payment_plan
    """
    payment_plans = [{1, 50.0}, {2, 30.0}]

    product_price = 120.0
    # TODO

def test_apply_payment_plans():
    """
    Test the apply_payment_plans function
        - Balance is correctly updated after applying payment plans
        - Payment plans are updated correctly
    """
    return None

def test_apply_discount():
    """
    Test the apply_discount function
        - Discount is applied correctly
        - Discount flag is set correctly
    """
    price = 100.0
    # check percent is calculated correctly, with a range
    # check final price is less than original price
    # check flag is correctly set 

    return None
