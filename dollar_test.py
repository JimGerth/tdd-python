import unittest
from dollar import Dollar
from franc import Franc


class DollarTest(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))


    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertFalse(Dollar(5) == Franc(5))
