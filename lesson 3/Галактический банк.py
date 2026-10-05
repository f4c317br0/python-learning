class CreditAccount:

    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def show_history(self):
        for el in self.history:
            print(el)

    def __add__(self, amount):
        new_acc = CreditAccount(self.balance + amount)
        new_acc.history = self.history.copy()
        new_acc.history.append(f"+{amount} кредитов")
        return new_acc

    def __sub__(self, amount):
        if amount > self.balance:
            raise ValueError("Не хватает кредитов! Иди подзаработай!")
        new_acc = CreditAccount(self.balance - amount)
        new_acc.history = self.history.copy()
        new_acc.history.append(f"-{amount} кредитов")
        return new_acc

    def __mul__(self, amount):
        new_balance = int(self.balance + self.balance * amount / 100)
        new_acc = CreditAccount(new_balance)
        new_acc.history = self.history.copy()
        new_acc.history.append(f"*{amount} (инвестиционный доход)")
        return new_acc

    def __str__(self):
        return f'Баланс: {self.balance} кредитов'


acc = CreditAccount(100)
acc = acc + 25
acc = acc * 10
acc = acc - 50
acc = acc + 100
for op in acc.history:
    print(op)
print(acc)
