import pytest
from BankAccount import BankAccount


def test_deposit():
    account = BankAccount("Ana", 100)
    account.deposit(50)

    assert account.getBalance() == 150


def test_withdraw():
    account = BankAccount("Ana", 100)
    account.withdraw(30)

    assert account.getBalance() == 70


def test_negative_withdraw():
    account = BankAccount("Ana", 100)

    with pytest.raises(ValueError):
        account.withdraw(-50)

    assert account.getBalance() == 100
