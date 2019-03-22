from unittest import TestCase
from nose.tools import assert_equal
from sol_5 import seq_gen

class test_1(TestCase):
    def test_1(self):
        expected=2520 
        result=seq_gen(10)
        assert_equal(result,expected)
