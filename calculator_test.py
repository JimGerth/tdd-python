import unittest
from calculator import Calculator
from money import Money


class CalculatorTets(unittest.TestCase):

    def test_addition(self):
        self.assertTrue(Calculator().add(Money.dollar(5), Money.dollar(5)) == Money.dollar(10))

    def test_subtractin(self):
        self.assertTrue(Calculator().subtract(Money.dollar(10), Money.dollar(5)) == Money.dollar(5))

    def test_multiplicatin(self):
        self.assertTrue(Calculator().multiply(Money.franc(10), 3) == Money.franc(30))