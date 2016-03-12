# -*- coding: utf-8 -*-

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return str(bin(n)).strip('0') == 'b1'
