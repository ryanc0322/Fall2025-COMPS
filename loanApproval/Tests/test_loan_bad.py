import pytest
import subprocess
from ProductionCode.loanApproval_bad import *

def test_get_employment(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    result = get_employment()
    assert isinstance(result, str)

def test_get_phone(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '123456789')
    result = get_phone()
    assert isinstance(result, int)

def test_get_address(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1219 Edgewood Street')
    result = get_address()
    assert isinstance(result, str)

def test_get_references(monkeypatch):
    inputs = iter(['123', 'Home1', '456', 'Home2', '789', 'Home3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_references()
    assert isinstance(result, list)
    assert isinstance(result[0], tuple)

def test_ask_questions(monkeypatch):
    inputs = iter(['yes', 'yes', 'yes'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = ask_questions()
    assert isinstance(result, list)
    assert isinstance(result[0], str)

def test_approval_accepted():
    result = approval(['yes', 'yes', 'yes'], 'yes', 'M')
    assert result == "Loan Accepted. Congrats."

def test_approval_not_employed():
    result = approval(['yes', 'yes', 'yes'], 'no', 'M')
    assert result == "Loan Denied, Sorry."

def test_approval_female():
    result = approval(['yes', 'yes', 'yes'], 'yes', 'F')
    assert result == "Loan Denied, Sorry."

def test_approval_answer_no():
    result = approval(['yes', 'no', 'yes'], 'yes', 'M')
    assert result == "Loan Denied, Sorry."