import pytest
import subprocess
from ProductionCode.loanApproval_good import *

def test_if_returns_approval_strong():
    result = approval([40, 40, 0, 30])
    assert result == "Loan Approved - Strong financial profile."
    
def test_if_returns_approval_mediocre():
    result = approval([40, 25, 0, 0])
    assert result == "Loan Under Review - Moderate profile, may need more information."
    
def test_if_returns_disapproval():
    result = approval([0, 0, 0, 0, 0])
    assert result == "Loan Denied - Insufficient financial stability."

def test_if_returns_thirty():
    result = get_assets(100000)
    assert result == 30
    
def test_if_returns_fifteen():
    result = get_assets(50000)
    assert result == 15

def test_if_returns_five():
    result = get_assets(20000)
    assert result == 5

def test_if_returns_zero():
    result = get_assets(0)
    assert result == 0

def test_if_returns_neg_forty():
    result = get_existing_loans(50000)
    assert result == -40
    
def test_if_returns_neg_twent_five():
    result = get_existing_loans(30000)
    assert result == -25

def test_if_returns_neg_ten():
    result = get_existing_loans(10000)
    assert result == -10

def test_if_returns_zero():
    result = get_existing_loans(0)
    assert result == 0

def test_if_returns_forty():
    result = get_monthly_income(7000)
    assert result == 40
    
def test_if_returns_twent_five():
    result = get_monthly_income(4000)
    assert result == 25

def test_if_returns_ten(self):
    result = get_monthly_income(2000)
    assert result == 10

def test_if_returns_zero(self):
    result = get_monthly_income(0)
    assert result == 0
