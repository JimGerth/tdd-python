
class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, money):
        return self.amount == money.amount and self._currency == money.currency()

    def __add__(self, addend):
        from sum import Sum
        return Sum(self, addend)

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def dollar(amount):
        return Money(amount, 'USD')

    def franc(amount):
        return Money(amount, 'CHF')

    def currency(self):
        return self._currency

    def reduce(self, bank, currency):
        return Money(self.amount / bank.rate(self.currency(), currency), currency)
