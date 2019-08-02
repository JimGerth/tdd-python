from money import Money

class Sum:

    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def reduce(self, currency):
        return Money(self._augend.amount + self._addend.amount, currency)