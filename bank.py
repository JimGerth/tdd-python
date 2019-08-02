from money import Money

class Bank:

    def __init__(self):
        self.rates = {}

    def reduce(self, expression, currency):
        try:
            result = expression.reduce(self, currency)
            return result
        except:
            print("could not reduce expression")

    def addRate(self, currency1, currency2 , rate):
        self.rates[(currency1, currency2)] = rate

    def rate(self, currency1, currency2):
        if currency1 == currency2: return 1
        return self.rates[(currency1, currency2)]