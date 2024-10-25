class BankAccount:
    def __init__(self, account_balance ):
      
        self.account_balance  = 0  # Default attribute value

    def deposit(self ,amount):
        self.account_balance = self.account_balance + amount


    def withdraw(self ,amount):
        res = self.account_balance - amount
        if res < 0:
         return False
        else:
         return True

    def display_balance(self):
        print(f" Current Balance:{self.account_balance} .")

