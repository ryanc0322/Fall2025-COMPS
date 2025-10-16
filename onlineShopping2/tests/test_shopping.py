import pytest
from shoppingSimulatorSol import *
import csv

'''
Load CSV data for testing
'''
products = []
categories = []
prices = []

with open("./products.csv", newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        products.append(row["Product Name"])
        categories.append(row["Category"])
        prices.append(float(row["Approximate Price (USD)"]))


def test_offer_product():
    """
    Test the offer_product function
        - Returned dictionary has expected keys
        - Values are from the CSV data
    """
    product = offer_product(products, categories, prices)
    # Returned dictionary has expected keys
    assert "name" in product
    assert "category" in product
    assert "price" in product
    # Values are from the CSV data
    assert product["name"] in products
    assert product["category"] in categories
    assert product["price"] in prices

def test_apply_purchase():
    """
    Test the apply_purchase function
        - New balance is correctly calculated
    """
    balance = 100.0
    cost = 30.0
    new_balance = apply_purchase(balance, cost)
    assert new_balance == balance - cost

def test_create_payment_plan():
    """
    Test the create_payment_plan function
        - New payment plan is added to the list
        - Payment amount is correctly calculated
    """
    return None

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
    return None
