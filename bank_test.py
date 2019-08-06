import unittest
from bank import Bank
from money import Money

class BankTest(unittest.TestCase):

    def setUp(self):
        self._bank = Bank()
        self._bank.addRate('CHF', 'USD', 2)

    def test_identity_rate(self):
        self.assertTrue(self._bank.rate('USD', 'USD') == 1)

    def test_custom_rate(self):
        self.assertTrue(self._bank.rate('CHF', 'USD') == 2)

    def test_inverse_rate(self):
        self.assertTrue(self._bank.rate('USD', 'CHF') == 0.5)

    def test_currency_conversion(self):
        self.assertTrue(self._bank.convert(Money.franc(10), 'USD') == Money.dollar(5))
        self.assertTrue(self._bank.convert(Money.dollar(5), 'CHF') == Money.franc(10))

    def test_simple_addition(self):
        self.assertTrue(self._bank.add(Money.dollar(5), Money.dollar(5)) == Money.dollar(10))

    def test_mixed_addition(self):
        self.assertTrue(self._bank.add(Money.dollar(5), Money.franc(10), 'USD') == Money.dollar(10))

    def test_multiple_addition(self):
        self.assertTrue(self._bank.add(self._bank.add(Money.dollar(5), Money.dollar(10)), Money.dollar(15)) == Money.dollar(30))

    def test_simple_multiplication(self):
        self.assertTrue(self._bank.multiply(Money.franc(10), 2) == Money.franc(20))

    def test_multiplication_of_sum(self):
        self.assertTrue(self._bank.multiply(Bank().add(Money.franc(5), Money.franc(5)), 3) == Money.franc(30))

    def test_subtraction(self):
        self.assertTrue(self._bank.subtract(Money.dollar(10), Money.dollar(5)) == Money.dollar(5))

    def test_multi_currency_comparison(self):
        self.assertTrue(self._bank.compare(Money.franc(10), Money.dollar(5)))
        self.assertFalse(self._bank.compare(Money.franc(5), Money.dollar(10)))