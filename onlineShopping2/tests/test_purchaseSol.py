import pytest
from purchaseSol import *
import csv

'''
Load CSV data for testing
'''
items = []
categories = []
prices = []

with open("purchaseItems.csv", newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        items.append(row["Product Name"])
        categories.append(row["Category"])
        prices.append(float(row["Approximate Price (USD)"]))

'''
Test the choose_item function
'''
def test_choose_item_keys_and_values():
    item = choose_item(items, categories, prices)
    # Check that all expected keys exist
    assert "name" in item
    assert "category" in item
    assert "base_price" in item
    assert "quality" in item
    # Check that values are from the csv
    assert item["name"] in items
    assert item["category"] in categories
    assert item["base_price"] in prices
    assert item["quality"] in QUALITY

