import pytest
import subprocess
from ProductionCode.loanApproval_better import *

def test_if_debt_is_string():
    monkeypatch.setattr('builtins.input', lambda _: ['yes', '1000', '2000', '3000'])
    result = get_debt()
    assert isinstance(result, list)
    assert len(result) == 3
    assert result == [1000, 2000, 3000]

def test_if_debt_is_string():
    monkeypatch.setattr('builtins.input', lambda _: ['no'])
    result = get_debt()
    assert isinstance(result, list)
    assert len(result) ==  3
    assert result == [0, 0, 0]

def test_if_asset_is_string():
    monkeypatch.setattr('builtins.input', lambda _: ['yes', '1000', '2000', '3000'])
    result = get_assets()
    assert isinstance(result, list)
    assert len(result) == 3
    assert result == [1000, 2000, 3000]

def test_if_debt_is_string():
    monkeypatch.setattr('builtins.input', lambda _: ['no'])
    result = get_assets()
    assert isinstance(result, list)
    assert len(result) == 3
    assert result == [0, 0, 0]

def test_if_returns_approval():
    result = approval([1000, 1000, 1000], [0, 0, 0], [25000, 20000, 10000])
    assert result == "Loan Approved - Strong salary, income, acceptable debts, and property value."

def test_if_returns_disapproval_high_debt():
    result = approval([1000, 1000, 1000], [50000, 2000, 0], [25000, 20000, 10000])
    assert result == "Loan Denied - Insufficient income or too much debt."

def test_if_returns_disapproval_low_income():
    result = approval([0, 0, 0], [0, 0, 0], [0, 0, 10000])
    assert result == "Loan Denied - Insufficient income or too much debt."

         

