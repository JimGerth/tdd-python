import unittest
from money import Money


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
        self.assertEqual(Money.franc(10).plus(Money.franc(10)), Money.franc(20))