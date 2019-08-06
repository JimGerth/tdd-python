import unittest
from money import Money


class MoneyTest(unittest.TestCase):

    def test_currency(self):
        self.assertTrue(Money.dollar(1).currency == 'USD')
        self.assertTrue(Money.franc(1).currency == 'CHF')

    def test_comparison(self):
        self.assertTrue(Money.dollar(1) == Money.dollar(1))
        self.assertFalse(Money.dollar(1) == Money.franc(1))
        self.assertFalse(Money.franc(1) == Money.franc(2))