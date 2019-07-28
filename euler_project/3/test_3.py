from unittest import TestCase
from nose.tools import assert_equal
from sol_3 import find_div


class interface_test(TestCase):
    def test_1(self):
        expected = [5, 7, 13, 29]
        result = find_div(13195)
        assert_equal(result, expected)
