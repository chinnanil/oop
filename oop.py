class Account:
    interest = 0.01
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
class Savings(Account):
    interest=0.5
    def __init__(self,holder):
        Account.__init__(self,holder)
save=Savings("ipsi")
print(save.holder)

