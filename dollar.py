class Dollar:

    def __init__(self, amount):
        self._amount = amount


    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


    def equals(self, dollar):
        return self.amount == dollar.amount


    def __eq__(self, dollar):
        return self.amount == dollar.amount
