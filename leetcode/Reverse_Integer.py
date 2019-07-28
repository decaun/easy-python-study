'''
https://leetcode.com/problems/reverse-integer/submissions/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            r = int(''.join(list(reversed(list(str(x))))))
        else:
            r = int('-'+''.join(list(reversed(list(str(abs(x)))))))

        if -2**31 < r < 2**31-1:
            return r
        else:
            return 0


'''
Runtime: 16 ms, faster than 99.00% of Python online submissions for Reverse Integer.
Memory Usage: 11.6 MB, less than 88.52% of Python online submissions for Reverse Integer.
'''
