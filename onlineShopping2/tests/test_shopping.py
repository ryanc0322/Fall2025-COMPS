import pytest
from solution_code.shopping_simulator_solution import *
import csv
import random

# ###########################################
# #          load data for testing          #
# ###########################################

products = []
categories = []
prices = []

with open('../student_facing_code/products.csv', newline='') as fh:
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
    assert apply_discount(100.0) is not None, "discount not implemented"

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
        if (products[i] == product["name"] and categories[i] == product["category"] and prices[i] == product["price"]):
            found = True
            break
    assert found, "Product not found in data."

def test_offer_product_randomness():
    """
    Test that offer_product returns random products. 
    """
    offers = set()
    for i in range(10):
        offer = offer_product(products, categories, prices)
        offers.add(offer["name"])
    assert len(offers) > 1, "offer_product should return random products."

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

def test_create_payment_plan_structure():
    """
    Test that create_payment_plan returns a list of dictionaries with num_payments and payment_amount.
    """
    payment_plans = payment_plans = [{"num_payments": 1, "payment_amount": 50.0}, {"num_payments": 2, "payment_amount": 30.0}]
    product_price = random.randint(10, 100)
    plan = create_payment_plan(payment_plans, product_price)

    assert isinstance(plan, list), "create_payment_plan should return a list."
    assert len(plan) == 3, "create_payment_plan should add one payment plan."
    assert isinstance(plan[0], dict), "Each payment plan should be a dictionary."
    assert "num_payments" in plan[0], "Payment plan dictionary should have 'num_payments' key."
    assert "payment_amount" in plan[0], "Payment plan dictionary should have 'payment_amount' key."

def test_create_payment_plan_amount():
    """
    Test payment_amount calculated in create_payment_plan
    """
    payment_plans = []
    product_price = random.randint(10, 100)
    plan = create_payment_plan(payment_plans, product_price)

    surcharge = product_price * 0.10
    payment_amount = (product_price + surcharge) / 3
    assert plan[0]["payment_amount"] == payment_amount, "payment_amount not calculated correctly."

# ###############################################
# #          apply_payment_plans tests          #
# ###############################################

def test_apply_payment_plans_total_payment():
    """
    Test that total_payment is correctly calculated and subtracted from balance
    """
    payment_plans = [{"num_payments": 1, "payment_amount": 50.0}, {"num_payments": 2, "payment_amount": 30.0}]
    balance = 200.0

    final_balance = balance - (50.0 + 30.0)

    test_balance, test_plans = apply_payment_plans(balance, payment_plans)
    assert test_balance == final_balance, "Total payment not calculated correctly and/or not subtracted from the balance."

def test_apply_payment_plans_decrement():
    """
    Test that num_payments is decremented correctly.
    """
    payment_plans = [{"num_payments": 1, "payment_amount": 50.0}, {"num_payments": 2, "payment_amount": 30.0}]
    balance = 200.0

    test_balance, test_plans = apply_payment_plans(balance, payment_plans)
    
    assert test_plans[0]["num_payments"] == 1, "num_payments not decremented correctly."

def test_apply_payment_plans_removal():
    """
    Test that finished payment plans are removed by apply_payment_plans.
    """
    payment_plans = [{"num_payments": 1, "payment_amount": 50.0}, {"num_payments": 2, "payment_amount": 30.0}]
    balance = 200.0

    test_balance, test_plans = apply_payment_plans(balance, payment_plans)

    assert len(test_plans) == 1, "Payment plans with num_payments=0 not removed."

# ##########################################
# #          apply_discount tests          #
# ##########################################

def test_apply_discount_random_apply():
    """
    Test the decision to apply discount is random.
    """
    price = 100.0
    discount = random.randint(5, 15) / 100
    flags = set()
    for i in range(10):
        final_price, discount_flag = apply_discount(price)
        flags.add(discount_flag)

    assert len(flags) == 2, "The discount should be applied randomly 50% of the time."

def test_apply_discount_random_value():
    """
    Test the percent discount applied is random between 5-15%.
    """
    price = 100.0
    discount = random.randint(5, 15) / 100
    discounted_prices = set()
    for i in range(10):
        final_price, discount_flag = apply_discount(price)
        if discount_flag == 1:
            discounted_prices.add(final_price)

    assert len(discounted_prices) > 0, "The percent discount applied should be a random value between 5-15%."

def test_apply_discount_flag():
    """
    Test that the discount_flag is set correctly.
    """
    price = 100.0
    for i in range(10):
        final_price, discount_flag = apply_discount(price)
        if final_price < price:
            assert discount_flag == 1, "discount_flag should be 1 when a discount is applied."
        else:
            assert discount_flag == 0, "discount_flag should be 0 when no discount is applied."

def test_apply_discount_correct_calculation():
    """
    Test that the discount is calculated correctly.
    """
    price = 100.0
    final_price, discount_flag = apply_discount(price)
    if discount_flag == 1:
        assert 85.0 <= final_price <= 95.0, "Discount not calculated correctly."
    else:
        assert final_price == price, "Price should remain the same when no discount is applied."

