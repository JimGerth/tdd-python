import unittest
from calculator import Calculator
from money import Money


class CalculatorTets(unittest.TestCase):

    def test_addition(self):
        self.assertTrue(Calculator().compare(Calculator().add(Money.dollar(5), Money.dollar(5)), Money.dollar(10)))

    def test_subtractin(self):
        self.assertTrue(Calculator().compare(Calculator().subtract(Money.dollar(10), Money.dollar(5)), Money.dollar(5)))

    def test_multiplicatin(self):
        self.assertTrue(Calculator().compare(Calculator().multiply(Money.franc(10), 3), Money.franc(30)))

    def test_comparison(self):
        self.assertTrue(Calculator().compare(Money.franc(10), Money.franc(10)))
        self.assertFalse(Calculator().compare(Money.franc(10), Money.dollar(10)))
        self.assertFalse(Calculator().compare(Money.dollar(5), Money.dollar(10)))