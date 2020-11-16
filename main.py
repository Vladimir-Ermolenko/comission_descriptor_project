
class Value:

    def __init__(self, value=None):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = int(value * (1 - instance.commission))


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
