from unittest import TestCase
from nose.tools import assert_equal
from sol_1 import multiples_3_5

class interface_test(TestCase):
    def test_1(self):
        expected=23
        result=multiples_3_5()
        assert_equal(result,expected)