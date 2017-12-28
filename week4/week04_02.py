
class Value():
    def __init__(self, amount=None):
        self.amount = amount

    def __get__(self, instance):
        return self.amount

    def __set__(self, instance, value):
        self.amount = value - value * instance.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)