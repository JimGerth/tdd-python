from hamcrest import *
import unittest
from bank import Bank
from money import Money

class BankTest(unittest.TestCase):

    def setUp(self):
        self._bank = Bank()
        self._bank.addRate('CHF', 'USD', 2)
        self._five_dollars = Money.dollar(5)
        self._ten_dollars = Money.dollar(10)
        self._fifteen_dollars = Money.dollar(15)
        self._five_francs = Money.franc(5)
        self._ten_francs = Money.franc(10)
        self._thirty_francs = Money.franc(30)

    def test_identity_rate(self):
        assert_that(self._bank.rate('USD', 'USD'), is_(equal_to(1)))

    def test_custom_rate(self):
        assert_that(self._bank.rate('CHF', 'USD'), is_(equal_to(2)))

    def test_inverse_rate(self):
        assert_that(self._bank.rate('USD', 'CHF'), is_(equal_to(0.5)))

    def test_currency_conversion(self):
        assert_that(self._bank.convert(self._ten_francs, to='USD'), is_(equal_to(self._five_dollars)))
        assert_that(self._bank.convert(self._five_dollars, to='CHF'), is_(equal_to(self._ten_francs)))

    def test_simple_addition(self):
        assert_that(self._bank.add(self._five_dollars, self._five_dollars), is_(equal_to(self._ten_dollars)))

    def test_mixed_addition(self):
        assert_that(self._bank.add(self._five_dollars, self._ten_francs, to='USD'), is_(equal_to(self._ten_dollars)))

    def test_multiple_addition(self):
        assert_that(self._bank.add(self._bank.add(self._five_dollars, self._five_dollars), self._five_dollars), is_(equal_to(self._fifteen_dollars)))

    def test_simple_multiplication(self):
        assert_that(self._bank.multiply(self._five_francs, by=2), is_(equal_to(self._ten_francs)))

    def test_multiplication_of_sum(self):
        assert_that(self._bank.multiply(self._bank.add(self._five_francs, self._five_francs), by=3), is_(equal_to(self._thirty_francs)))

    def test_subtraction(self):
        assert_that(self._bank.subtract(self._ten_dollars, self._five_dollars), is_(equal_to(self._five_dollars)))

    def test_multi_currency_comparison(self):
        assert_that(self._bank.compare(self._ten_francs, to=self._five_dollars), is_(True))
        assert_that(self._bank.compare(self._five_francs, to=self._ten_dollars), is_(False))