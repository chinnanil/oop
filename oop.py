class Account:
    interest = 0.02
    def __init__(self,holder):
        self.holder=holder
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            return self.balance
        else :

            return "insufficient balance"
a=Account("anil")
a.deposit(500)

class CheckingAccount(Account,Bank):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return super().withdraw(amount+CheckingAccount.withdraw_fee)

ch=CheckingAccount("ipsi")
print(ch.withdraw(200))
