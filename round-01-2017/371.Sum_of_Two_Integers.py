# -*- coding: utf-8 -*-


class Solution(object):
    MASK = 0xFFFFFFFF
    MAX = 0x7FFFFFFF

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a if a <= self.MAX else ~(a ^ self.MASK)
        a, b = (a ^ b) & self.MASK, ((a & b) << 1) & self.MASK
        return self.getSum(a, b)
