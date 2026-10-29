class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

        return self.balance


    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"

        else:
            self.balance -= amount
            return self.balance

    def __repr__(self):
        return f"BankAccount(name='{self.name}', balance={self.balance})"

user1 = BankAccount("Amit", 5000)

print(user1.deposit(1500))

print(user1.withdraw(2000))

print(user1.withdraw(10000))

print(user1)

