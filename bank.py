from money import Money

class Bank:

    def reduce(self, expression, currency):
        try:
            result = expression.reduce(currency)
        except:
            print("could not reduce expression")
        return result