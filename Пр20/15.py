class BankAccount:
    __slots__ = ('balance',)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Not enough money")
        self.balance -= amount

acc = BankAccount()
acc.balance = 100

acc.deposit(50)
print(acc.balance)

acc.withdraw(30)
print(acc.balance)

try:
    acc.withdraw(200)
except ValueError as e:
    print(e)
