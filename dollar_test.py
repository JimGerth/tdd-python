import unittest
from money import Money


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
        self.assertTrue(Money(10, 'USD') == Money.dollar(10))
