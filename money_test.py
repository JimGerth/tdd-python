from hamcrest import *
import unittest
from money import Money


class MoneyTest(unittest.TestCase):

    def setUp(self):
        self._one_dollar = Money.dollar(1)
        self._one_franc = Money.franc(1)
        self._two_francs = Money.franc(2)

    def test_currency(self):
        assert_that(self._one_dollar.currency, is_('USD'))
        assert_that(self._one_franc.currency, is_('CHF'))

    def test_comparison(self):
        assert_that(self._one_dollar, is_(equal_to(self._one_dollar)))
        assert_that(self._one_dollar, is_(not_(equal_to(self._one_franc))))
        assert_that(self._one_franc, is_(not_(equal_to(self._two_francs))))