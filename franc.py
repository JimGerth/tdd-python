class Franc:

    def __init__(self, amount):
        self._amount = amount


    def times(self, multiplier):
        return Franc(self._amount * multiplier)


    def __eq__(self, franc):
        return self._amount == franc._amount
