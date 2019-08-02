from money import Money

class Sum:

    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def reduce(self, bank, currency):
        return Money(bank.reduce(self._augend, currency).amount + bank.reduce(self._addend, currency).amount, currency)

    def plus(self, addend):
        return Sum(self, addend)