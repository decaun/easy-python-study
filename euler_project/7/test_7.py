from unittest import TestCase
from nose.tools import assert_equal
from sol_7 import prime

class interface_test(TestCase):
    def test_1(self):
        expected=2
        result=prime(0)
        assert_equal(result,expected)
        
    def test_2(self):
        expected=3
        result=prime(2)
        assert_equal(result,expected)
        
    def test_3(self):
        expected=5
        result=prime(3)
        assert_equal(result,expected)
        
    def test_4(self):
        expected=7
        result=prime(4)
        assert_equal(result,expected)

    def test_5(self):
        expected=11
        result=prime(5)
        assert_equal(result,expected)

    def test_6(self):
        expected=3571
        result=prime(500)
        assert_equal(result,expected)
        
    def test_7(self):
        expected=5503
        result=prime(727)
        assert_equal(result,expected)


