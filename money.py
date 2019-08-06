
class Money:

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        assert type(self) == Money
        return self._amount

    @property
    def currency(self):
        assert type(self) == Money
        return self._currency

    def __eq__(self, money):
        return self.amount == money.amount and self.currency == money.currency

    def __add__(self, addend):
        from sum import Sum
        return Sum(self, addend)

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def dollar(amount):
        return Money(amount, 'USD')

    def franc(amount):
        return Money(amount, 'CHF')

    def reduce(self, bank, currency):
        return Money(self.amount / bank.rate(self.currency, currency), currency)
