import unittest
from calculator import Calculator
from money import Money


class CalculatorTets(unittest.TestCase):
    
    def test_addition(self):
        self.assertTrue(Calculator().add(Money.dollar(5), Money.dollar(5)) == Money.dollar(10))