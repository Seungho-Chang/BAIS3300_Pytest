import pytest
from oop_loan_pmt import *

###unit test###

def test_calculateDiscountFactor():
    """
    Given loan amount, years, and interest
    THEN calculate discount factor
    """
    loan = Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    assert loan.getDiscountFactor() == pytest.approx(166.791, rel=1e-3)

def test_calculateLoanPmt():
    """
    Given loan amount, years, and interst
    THEN calculate loan payment
    """
    loan = Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    assert loan.getLoanPmt() == pytest.approx(599.55, 0.01)

###functional test###

def test_collectLoanDetails(monkeypatch):
    input_str = '100000\n30\n0.06\n'
    monkeypatch.setattr('builtins.input', lambda x: input_str)
    result = collectLoanDetails()
    assert result.loanAmount == 100000.0
    assert result.numberYears == 30.0
    assert result.annualRate == 0.06

def test_main():
    with patch('builtins.input', side_effect=['100000', '30', '0.06']):
        captured_output = io.StringIO()          
        sys.stdout = captured_output               
        main()                                     
        sys.stdout = sys.__stdout__                 
        assert captured_output.getvalue().strip() == 'Your monthly payment is: $599.55'
