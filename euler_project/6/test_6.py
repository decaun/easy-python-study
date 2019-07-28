from unittest import TestCase
from nose.tools import assert_equal
from sol_6 import sos_diff, sum_of_squares, square_of_sum


class interface_test(TestCase):
    def test_1(self):
        expected = 385
        result = sum_of_squares(10)
        assert_equal(result, expected)

    def test_2(self):
        expected = 3025
        result = square_of_sum(10)
        assert_equal(result, expected)

    def test_3(self):
        expected = 2640
        result = sos_diff(10)
        assert_equal(result, expected)
