class Bank():
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f'Your updated balance is {self.balance}'
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f'Your updated balance is {self.balance}'
        else:
            return f'Not enough money!'
    def get_balance(self):
        return self.balance
q = Bank(0)
i = int(input("What do u want to do?\nPress 1 to add money\nPress 2 to substract money\nPress 3 to see the current balance\n"))
while i!=0: 
    if i == 1: 
        amount = int(input("Choose the amount:\n"))
        print(q.deposit(amount))
    elif i ==2:  
        amount = int(input("Choose the amount:\n"))
        print(q.withdraw(amount))
    else:
        print(f"Your current balance:{q.get_balance()}")
    i = int(input())
