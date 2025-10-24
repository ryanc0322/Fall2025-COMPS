import pytest
import subprocess
from ProductionCode.loanApproval_mediocre import *

def test_if_returns_approval():
    result = approval([1, 1, 1, 0, 1])
    assert result == "Loan Approved"

def test_if_returns_disapproval():
    result = approval([0, 0, 1, 0, 1])
    assert result == "Loan Denied"

def test_if_returns_one():
    result = get_assets('yes')
    assert result == 1
    
def test_if_returns_zero():
    result = get_assets('no')
    assert result == 0

def test_if_returns_one():
    result = get_existing_loans('yes')
    assert result == -1
    
def test_if_returns_zero():
    result = get_existing_loans('no')
    assert result == 0

def test_if_returns_one():
    result = get_monthly_income('yes')
    assert result == 1

def test_if_returns_zero():
    result = get_monthly_income('no')
    assert result == 0

def test_if_returns_one():
    result = get_job_stability('yes')
    assert result == 1
    
def test_if_returns_zero():
    result = get_job_stability('no')
    assert result == 0