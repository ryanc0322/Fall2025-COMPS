import unittest
import subprocess
from ProductionCode.loanApproval_good import *

class Testapproval(unittest.TestCase):
    def test_if_returns_approval_strong(self):
         result = approval([40, 40, 0, 30])
         self.assertEqual(result, "Loan Approved - Strong financial profile.")
    
    def test_if_returns_approval_mediocre(self):
        result = approval([40, 25, 0, 0])
        self.assertEqual(result, "Loan Under Review - Moderate profile, may need more information.")
    
class Testdisapproval(unittest.TestCase):
    def test_if_returns_disapproval(self):
         result = approval([0, 0, 0, 0, 0])
         self.assertEqual(result, "Loan Denied - Insufficient financial stability.")

class Testget_assets(unittest.TestCase):
    def test_if_returns_thirty(self):
        result = get_assets(100000)
        self.assertEqual(result, 30)
    
    def test_if_returns_fifteen(self):
        result = get_assets(50000)
        self.assertEqual(result, 15)

    def test_if_returns_five(self):
        result = get_assets(20000)
        self.assertEqual(result, 5)

    def test_if_returns_zero(self):
        result = get_assets(0)
        self.assertEqual(result, 0)

class Testget_existing_loans(unittest.TestCase):
    def test_if_returns_neg_forty(self):
        result = get_existing_loans(50000)
        self.assertEqual(result, -40)
    
    def test_if_returns_neg_twent_five(self):
        result = get_existing_loans(30000)
        self.assertEqual(result, -25)

    def test_if_returns_neg_ten(self):
        result = get_existing_loans(10000)
        self.assertEqual(result, -10)

    def test_if_returns_zero(self):
        result = get_existing_loans(0)
        self.assertEqual(result, 0)

class Testget_monthly_income(unittest.TestCase):
    def test_if_returns_forty(self):
        result = get_monthly_income(7000)
        self.assertEqual(result, 40)
    
    def test_if_returns_twent_five(self):
        result = get_monthly_income(4000)
        self.assertEqual(result, 25)

    def test_if_returns_ten(self):
        result = get_monthly_income(2000)
        self.assertEqual(result, 10)

    def test_if_returns_zero(self):
        result = get_monthly_income(0)
        self.assertEqual(result, 0)
