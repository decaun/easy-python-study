from unittest import TestCase
from nose.tools import assert_equal
from sol_8 import greatest_product


class interface_test(TestCase):
    def test_1(self):
        expected = 5832
        result = greatest_product(4)
        assert_equal(result, expected)
