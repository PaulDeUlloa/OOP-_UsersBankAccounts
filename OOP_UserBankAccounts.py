class BankAccount:
    all_account = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account.append(self)

    def account_balance(self):
        print(f"Your current balance is: ${self.balance}")
        return self

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self):
        self.account.deposit(100)
        print(f"Account balance: ${self.account.balance}")

    def make_withdraw(self):
        self.account.withdraw(35)
        print(f"Withdraw complete, account balance: ${self.account.balance}")

    def display_user_balance(self):
        print(f"Your current account balance: ${self.account.balance}")

Paul = User("Paul De Ulloa", "Pauld@CodingDojo.com")
Paul.make_deposit()
Paul.make_withdraw()
Paul.display_user_balance()