import unittest
from calculator import Calculator
from money import Money


class CalculatorTets(unittest.TestCase):

    def setUp(self):
        self._calc = Calculator()

    def test_addition(self):
        self.assertTrue(self._calc.add(Money.dollar(5), Money.dollar(5)) == Money.dollar(10))

    def test_subtractin(self):
        self.assertTrue(self._calc.subtract(Money.dollar(10), Money.dollar(5)) == Money.dollar(5))

    def test_multiplicatin(self):
        self.assertTrue(self._calc.multiply(Money.franc(10), 3) == Money.franc(30))

    def test_comparison(self):
        self.assertTrue(self._calc.compare(Money.franc(10), Money.franc(10)))
        self.assertFalse(self._calc.compare(Money.franc(10), Money.dollar(10)))
        self.assertFalse(self._calc.compare(Money.dollar(5), Money.dollar(10)))