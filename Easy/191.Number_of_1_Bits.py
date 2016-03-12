# -*- coding: utf-8 -*-


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_str = str(bin(n))
        return len([x for x in binary_str[2:] if x == '1'])
