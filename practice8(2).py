#Create Account class with 2 attributes - balance and account number.
#Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc 

    def credit(self, amount):
        self.balance += amount
        print("Taka", amount, "is credited to your account. Now your balance is", self.get_balance() )

    def debit(self, amount):
        self.balance -= amount
        print("Taka", amount, "is debited from your account. Now your balance is", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 112259)
print("Hello, your accoutn number is : ", acc1.account_no)
print("Your current balance is : ", acc1.get_balance())

acc1.credit(30000)
acc1.debit(10000)
acc1.debit(5000)
acc1.credit(2000)
