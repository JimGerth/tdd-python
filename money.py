
class Money:

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, money):
        return self._amount == money._amount and self.__class__ == money.__class__

    def dollar(amount):
        from dollar import Dollar
        return Dollar(amount)

    def franc(amount):
        from franc import Franc
        return Franc(amount)
