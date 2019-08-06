import unittest
from bank import Bank

class BankTest(unittest.TestCase):

    def test_identity_rate(self):
        self.assertTrue(Bank().rate('USD', 'USD') == 1)

    def test_custom_rate(self):
        bank = Bank()
        bank.addRate('USD', 'CHF', 2)
        self.assertTrue(bank.rate('USD', 'CHF') == 2)