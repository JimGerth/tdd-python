from calculator import Calculator
from money import Money

class Bank:

    def __init__(self):
        self.rates = {}
        self.calc = Calculator()

    def reduce(self, expression, currency):
        try:
            result = expression.reduce(self, currency)
            return result
        except:
            print("could not reduce expression")

    def addRate(self, currency1, currency2 , rate):
        self.rates[(currency1, currency2)] = rate
        self.rates[(currency2, currency1)] = 1 / rate

    def rate(self, currency1, currency2):
        if currency1 == currency2: return 1
        return self.rates[(currency1, currency2)]

    def convert(self, money, to):
        if money.currency == to:
            return money
        return Money(money.amount / self.rate(money.currency, to), to)

    def add(self, money1, money2, currency=None):
        if not currency:
            assert money1.currency == money2.currency
            currency = money1.currency
        return self.calc.add(self.convert(money1, currency), self.convert(money2, currency))

    def multiply(self, money, by, currency=None):
        if not currency:
            currency = money.currency
        return self.calc.multiply(self.convert(money, currency), by)

    def subtract(self, money1, money2, currency=None):
        if not currency:
            assert money1.currency == money2.currency
            currency = money1.currency
        return self.calc.subtract(self.convert(money1, currency), self.convert(money2, currency))

    def compare(self, money1, money2):
        return self.calc.compare(money1, self.convert(money2, money1.currency))
