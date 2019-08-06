import unittest
from bank import Bank
from money import Money

class BankTest(unittest.TestCase):

    def test_identity_rate(self):
        self.assertTrue(Bank().rate('USD', 'USD') == 1)

    def test_custom_rate(self):
        bank = Bank()
        bank.addRate('USD', 'CHF', 2)
        self.assertTrue(bank.rate('USD', 'CHF') == 2)

    def test_currency_conversion(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        self.assertTrue(bank.convert(Money.franc(10), 'USD') == Money.dollar(5))

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