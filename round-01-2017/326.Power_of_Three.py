# -*- coding: utf-8 -*-


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while True:
            if n >= 3:
                n /= 3.0
            else:
                return n == 1

