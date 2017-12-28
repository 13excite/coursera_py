
class Value():
    def __init__(self, amount=None):
        self.amount = amount

    def __get__(self, xz):
        pass

    def __set__(self, xz):
        pass


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission