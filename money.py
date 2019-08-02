
class Money:

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, money):
        return self._amount == money._amount and self._currency == money.currency()

    def dollar(amount):
        from dollar import Dollar
        return Dollar(amount, 'USD')

    def franc(amount):
        from franc import Franc
        return Franc(amount, 'CHF')

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

