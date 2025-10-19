import unittest
import subprocess
from unittest.mock import patch
from ProductionCode.loanApproval_bad import *

class Testget_employment(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes'])
    def test_if_input_is_string(self, mock_input):
         result = get_employment()
         self.assertIsInstance(result, str)

class Testget_phone(unittest.TestCase):
    @patch('builtins.input', side_effect=['123456789'])
    def test_if_input_is_num(self, mock_input):
         result = get_phone()
         self.assertIsInstance(result, int)

class Testget_address(unittest.TestCase):
    @patch('builtins.input', side_effect=['1219 Edgewood Street'])
    def test_if_input_is_a_string(self, mock_input):
        result = get_address()
        self.assertIsInstance(result, str)

class Testget_references(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '123', 'Home1',
        '456', 'Home2',
        '789', 'Home3'])
    def test_if_input_is_list_of_tuples(self, mock_input) :
        result = get_references()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

class Testask_questions(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes', 'yes', 'yes'])
    def test_if_input_is_list_of_strings(self, mock_input):
         result = ask_questions()
         self.assertIsInstance(result, list)
         self.assertIsInstance(result[0], str)

class Testapproval(unittest.TestCase):
    def test_if_returns_approval(self):
         result = approval(['yes', 'yes', 'yes'], 'yes', 'M')
         self.assertEqual(result, "Loan Accepted. Congrats.")

class Testapproval_not_approved(unittest.TestCase):
    def test_if_returns_disapproval_not_employed(self):
         result = approval(['yes', 'yes', 'yes'], 'no', 'M')
         self.assertEqual(result, "Loan Denied, Sorry.")
    
    def test_if_returns_disapproval_woman(self):
       result = approval(['yes', 'yes', 'yes'], 'yes', 'F')
       self.assertEqual(result, "Loan Denied, Sorry.")
    
    def test_if_returns_disapproval_answer_no(self):
        result = approval(['yes', 'no', 'yes'], 'yes', 'M')
        self.assertEqual(result, "Loan Denied, Sorry.")
