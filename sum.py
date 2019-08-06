from money import Money

class Sum:

    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def __add__(self, addend):
        return Sum(self, addend)

    def __mul__(self, multiplier):
        return Sum(self._augend * multiplier, self._addend * multiplier)

    def reduce(self, bank, currency):
        return Money(bank.reduce(self._augend, currency).amount + bank.reduce(self._addend, currency).amount, currency)