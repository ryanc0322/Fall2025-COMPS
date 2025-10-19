import unittest
import subprocess
from unittest.mock import patch
from ProductionCode.loanApproval_better import *

class Testget_debt(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes', '1000', '2000', '3000'])
    def test_if_debt_is_string(self, mock_input):
        result = get_debt()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [1000, 2000, 3000])

class Testget_debtNo(unittest.TestCase):
    @patch('builtins.input', side_effect=['no'])
    def test_if_debt_is_string(self, mock_input):
        result = get_debt()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [0, 0, 0])

class Testget_assets(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes', '1000', '2000', '3000'])
    def test_if_asset_is_string(self, mock_input):
        result = get_assets()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [1000, 2000, 3000])

class Testget_assetsNo(unittest.TestCase):
    @patch('builtins.input', side_effect=['no'])
    def test_if_debt_is_string(self, mock_input):
        result = get_assets()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [0, 0, 0])

class Testapproval(unittest.TestCase):
    def test_if_returns_approval(self):
        result = approval([1000, 1000, 1000], [0, 0, 0], [25000, 20000, 10000])
        self.assertEqual(result, "Loan Approved - Strong salary, income, acceptable debts, and property value.")

class Testapproval_not_approved(unittest.TestCase):
    def test_if_returns_disapproval_high_debt(self):
        result = approval([1000, 1000, 1000], [50000, 2000, 0], [25000, 20000, 10000])
        self.assertEqual(result, "Loan Denied - Insufficient income or too much debt.")

    def test_if_returns_disapproval_low_income(self):
        result = approval([0, 0, 0], [0, 0, 0], [0, 0, 10000])
        self.assertEqual(result, "Loan Denied - Insufficient income or too much debt.")

         

