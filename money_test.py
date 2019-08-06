import unittest
from money import Money
from bank import Bank

class MoneyTest(unittest.TestCase):

    def test_money(self):
        pass

    def test_currency(self):
        self.assertTrue(Money.dollar(1).currency() == 'USD')
        self.assertTrue(Money.franc(1).currency() == 'CHF')

    def test_comparison(self):
        self.assertTrue(Money.dollar(1) == Money.dollar(1))
        self.assertFalse(Money.dollar(1) == Money.franc(1))
        self.assertFalse(Money.franc(1) == Money.franc(2))

    def test_currency_conversion(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        self.assertTrue(bank.reduce(Money.franc(10), 'USD') == Money.dollar(5))

    def test_simple_addition(self):
        self.assertTrue(Bank().reduce(Money.dollar(5) + Money.dollar(5), 'USD') == Money.dollar(10))

    def test_mixed_addition(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        self.assertTrue(bank.reduce(Money.dollar(5) + Money.franc(10), 'USD') == Money.dollar(10))

    def test_multiple_addition(self):
        self.assertTrue(Bank().reduce(Money.dollar(5) + Money.dollar(10) + Money.dollar(15), 'USD') == Money.dollar(30))

    def test_simple_multiplication(self):
        self.assertTrue(Bank().reduce(Money.franc(10) * 2, 'CHF') == Money.franc(20))

    def test_multiplication_of_sum(self):
        self.assertTrue(Bank().reduce((Money.franc(5) + Money.franc(5)) * 3, 'CHF') == Money.franc(30))