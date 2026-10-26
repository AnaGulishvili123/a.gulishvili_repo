
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.__owner = owner
        self.__balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def getBalance(self):
        return self.__balance


# Create an account
account = BankAccount("Ana", 100.0)

# Deposit money
account.deposit(50)

# Withdraw money
account.withdraw(30)

# Check balance
print(account.getBalance())