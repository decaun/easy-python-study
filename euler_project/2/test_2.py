from unittest import TestCase
from nose.tools import assert_equal
from sol_2 import fibonacci

class test_1(TestCase):
    def test_1(self):
        expected=[1, 2, 3, 5, 8]
        result=list(fibonacci(6))
        assert_equal(result,expected)