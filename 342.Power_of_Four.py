# -*- coding: utf-8 -*-

"""
Given an integer (signed 32 bits), write a function to check whether it is
a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bit = bin(num)[2:]
        zero_len = len(bit) - 1
        return bit[0] == '1' and zero_len % 2 == 0 and bit[1:] == ('0' * zero_len)

