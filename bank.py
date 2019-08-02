from money import Money

class Bank:

    def reduce(self, expression, currency):
        return expression.reduce(currency)