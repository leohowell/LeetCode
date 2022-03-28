# -*- coding: utf-8 -*-

"""
You have a total of n coins that you want to form in a staircase shape,
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed
integer.


Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        elif n in (3, 4):
            return 2
        elif n < 8:
            return n / 2

        low = 0
        high = n / 2
        while low < high:
            mid = (low + high) / 2
            if mid * (mid + 1) / 2 > n:
                high = mid
            else:
                low = mid + 1
        return low - 1
