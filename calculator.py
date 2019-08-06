from money import Money


class Calculator:

    def add(self, money1, money2):
        assert money1.currency == money2.currency
        return Money(money1.amount + money2.amount, money1.currency)