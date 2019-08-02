import unittest
from money import Money
from bank import Bank


class FrancTest(unittest.TestCase):

    def test_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def test_currency(self):
        self.assertEqual('CHF', Money.franc(1).currency())

    def test_simple_addition(self):
        self.assertTrue(Bank().reduce(Money.franc(1), 'CHF') == Money.franc(1))
        self.assertTrue(Bank().reduce(Money.franc(5).plus(Money.franc(5)), 'CHF') == Money.franc(10))
        self.assertTrue(Bank().reduce(Money.franc(10).plus(Money.franc(10)), 'CHF') == Money.franc(20))

    def test_currency_conversion(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        self.assertTrue(bank.reduce(Money.franc(2), 'USD') == Money.dollar(1))

    def test_identity_rate(self):
        self.assertTrue(Bank().rate('CHF', 'CHF') == 1)