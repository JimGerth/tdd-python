
class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, money):
        return self.amount == money.amount and self._currency == money.currency()

    def dollar(amount):
        return Money(amount, 'USD')

    def franc(amount):
        return Money(amount, 'CHF')

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def plus(self, addend):
        from sum import Sum
        return Sum(self, addend)

    def reduce(self, bank, currency):
        return Money(self.amount / bank.rate(self.currency(), currency), currency)
