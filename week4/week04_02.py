
class Value():
    def __init__(self, amount=None):
        self.amount = amount

    def __get__(self):
        return self.amount

    def __set__(self, instance, value):
        self.amount = value - value * instance.commisson


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

