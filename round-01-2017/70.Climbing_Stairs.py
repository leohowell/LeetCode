# -*- coding: utf-8 -*-

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
"""


class Solution(object):
    CACHE = {
        1: 1,
        2: 2,
    }

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = self.CACHE.get(n)
        if not r:
            r = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.CACHE[n] = r
        return r
