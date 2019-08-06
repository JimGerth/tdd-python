
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

    def dollar(amount):
        return Money(amount, 'USD')

    def franc(amount):
        return Money(amount, 'CHF')
