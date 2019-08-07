from hamcrest import *
import unittest
from calculator import Calculator
from money import Money


class CalculatorTets(unittest.TestCase):

    def setUp(self):
        self._calc = Calculator()
        self._five_dollars = Money.dollar(5)
        self._ten_dollars = Money.dollar(10)
        self._thirty_dollars = Money.dollar(30)
        self._ten_francs = Money.franc(10)

    def test_addition(self):
        assert_that(self._calc.add(self._five_dollars, self._five_dollars), is_(equal_to(self._ten_dollars)))

    def test_subtractin(self):
        assert_that(self._calc.subtract(self._ten_dollars, self._five_dollars), is_(equal_to(self._five_dollars)))

    def test_multiplicatin(self):
        self.assertTrue(self._calc.multiply(Money.franc(10), 3) == Money.franc(30))
        assert_that(self._calc.multiply(self._ten_dollars, by=3), is_(equal_to(self._thirty_dollars)))

    def test_comparison(self):
        assert_that(self._calc.compare(self._ten_dollars, to=self._ten_dollars), is_(True))
        assert_that(self._calc.compare(self._ten_francs, to=self._ten_dollars), is_(False))
        assert_that(self._calc.compare(self._five_dollars, to=self._ten_dollars), is_(False))