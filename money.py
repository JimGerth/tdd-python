class Money:

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, money):
        return self._amount == money._amount