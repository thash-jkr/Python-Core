class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\n' + f'Account Balance: $ {self.balance}'

    def deposit(self, dep_amount=0):
        self.balance = self.balance + dep_amount
        print(f'$ {dep_amount} is deposited.')

    def withdraw(self, with_amount=0):
        if with_amount > self.balance:
            print(f'Failed!\nYour balance is only {self.balance}')
        else:
            self.balance = self.balance - with_amount
            print("Withdrawal Accepted")


acc1 = Account('Jose', 1000)
print(acc1)
acc1.deposit(10000)
print(acc1.balance)
acc1.withdraw(9876)
print(acc1.balance)
acc1.withdraw(2000)
