class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance <= 0:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance} Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self

account1 = BankAccount(1.05, 0)

account1.deposit(100).deposit(100).deposit(100).yield_interest().display_account_info()


account2 = BankAccount(1.05, 0)

account2.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()