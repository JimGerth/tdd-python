import unittest
from money import Money
from bank import Bank


class DollarTest(unittest.TestCase):

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())

    def test_simple_addition(self):
        self.assertTrue(Bank().reduce(Money.dollar(1), 'USD') == Money.dollar(1))
        self.assertTrue(Bank().reduce(Money.dollar(5).plus(Money.dollar(5)), 'USD') == Money.dollar(10))
        self.assertTrue(Bank().reduce(Money.dollar(10).plus(Money.dollar(10)), 'USD') == Money.dollar(20))

    def test_currency_conversion(self):
        bank = Bank()
        bank.addRate('USD', 'CHF', 2)
        self.assertTrue(bank.reduce(Money.dollar(2), 'CHF') == Money.franc(1))

    def test_identity_rate(self):
        self.assertTrue(Bank().rate('USD', 'USD') == 1)