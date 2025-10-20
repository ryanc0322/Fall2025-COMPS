import unittest
import subprocess
from ProductionCode.loanApproval_mediocre import *

class Testapproval(unittest.TestCase):
    def test_if_returns_approval(self):
         result = approval([1, 1, 1, 0, 1])
         self.assertEqual(result, "Loan Approved")

class Testdisapproval(unittest.TestCase):
    def test_if_returns_disapproval(self):
         result = approval([0, 0, 1, 0, 1])
         self.assertEqual(result, "Loan Denied")

class Testget_assets(unittest.TestCase):
    def test_if_returns_one(self):
         result = get_assets('yes')
         self.assertEqual(result, 1)
    
    def test_if_returns_zero(self):
         result = get_assets('no')
         self.assertEqual(result, 0)

class Testget_existing_loans(unittest.TestCase):
    def test_if_returns_one(self):
         result = get_existing_loans('yes')
         self.assertEqual(result, -1)
    
    def test_if_returns_zero(self):
         result = get_existing_loans('no')
         self.assertEqual(result, 0)

class Testget_monthly_income(unittest.TestCase):
    def test_if_returns_one(self):
         result = get_monthly_income('yes')
         self.assertEqual(result, 1)

    def test_if_returns_zero(self):
         result = get_monthly_income('no')
         self.assertEqual(result, 0)

class Testget_job_stability(unittest.TestCase):
    def test_if_returns_one(self):
         result = get_job_stability('yes')
         self.assertEqual(result, 1)
    
    def test_if_returns_zero(self):
         result = get_job_stability('no')
         self.assertEqual(result, 0)