# OOP exercise 1
import uuid
class BankAccount():
    def __init__(self, HolderName):
        self.HolderName = HolderName
        self.balance = 0
        self.account_number = RandomAccNum()

    def __str__(self):
        return f"{self.HolderName}'s Account ({self.account_number}), Balance: {self.balance}$"
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"You deposited {amount} in your bank account!, Current Balance: {self.balance}$")
        else:
            print(f"Invaild number!, Cannot deposit {amount}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"You're trying to withdraw {amount}$ which is not possible!, Current Balance: {self.balance}$")
        else:
            self.balance - amount
            print(f"You withdraw {self.balance - amount}$, Good luck!")

def RandomAccNum():
    return uuid.uuid4()

new_account = BankAccount("Singular")
print(new_account)
new_account.deposit(20)
new_account.deposit(20)
new_account.withdraw(20)
print(new_account)
new_account.withdraw(2000)
#new_account.deposit("Apple")
