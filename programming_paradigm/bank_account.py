class BankAccount:
    def __init__(self, account_balance ):
      
        self.account_balance  = 0  # Default attribute value

    def deposit(self ,amount):
        self.account_balance = self.account_balance + amount


    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")


    def display_balance(self):
        print(f" Current Balance:${self.account_balance} .")

