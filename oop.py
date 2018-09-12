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
            return "insufficient blance"
