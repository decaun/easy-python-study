# from shell run python3 -m "nose" tests.py
# or 1st install nosetests3 from apt-get > sudo apt-get install python-nose python3-nose
# 2nd sudo python3 -m pip install -U mock
# 3rd sudo python3 -m pip install nose
# then issue command nosetests3 tests.py / nosetests tests.py / python3 -m nose test_2.py

from unittest import TestCase  # 1
from mock import patch, call  # 2
from nose.tools import assert_equal, assert_list_equal  # 3
from filter_funcs import filter_ints, is_positive  # 4


class FilterIntsTestCase(TestCase):  # 5

    '''interface test'''

    def test_filter_ints_return_value(self):
        v = [3, -4, 0, -2, 5, 0, 8, -1]
        result = filter_ints(v)
        assert_list_equal([3, 5, 8], result)

    '''interface test with triangulation'''

    def test_filter_ints_return_value_triangular(self):
        v1 = [3, -4, 0, -2, 5, 0, 8, -1]
        v2 = [7, -3, 0, 0, 9, 1]
        assert_list_equal([3, 5, 8], filter_ints(v1))
        assert_list_equal([7, 9, 1], filter_ints(v2))

    '''interface test with boundaries'''

    def test_is_positive(self):
        # before boundary with granularity 1
        assert_equal(False, is_positive(-1))
        # on the boundary with granularity 1
        assert_equal(False, is_positive(0))
        # after the boundary with granularity 1
        assert_equal(True, is_positive(1))

    def test_is_positive_v2(self):
        assert_equal(False, is_positive(0))
        for n in range(1, 10 ** 4):
            assert_equal(False, is_positive(-n))
            assert_equal(True, is_positive(n))

    '''unit test'''
    @patch('filter_funcs.is_positive')  # 6
    def test_filter_ints(self, is_positive_mock):  # 7
        # preparation
        v = [3, -4, 0, 5, 8]
        # execution
        filter_ints(v)  # 8
        # verification
        assert_equal(
            [call(3), call(-4), call(0), call(5), call(8)],
            is_positive_mock.call_args_list
        )  # 9
