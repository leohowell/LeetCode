# -*- coding: utf-8 -*-

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise
# return 0

import time


def guess(num):
    if num == 2:
        return 0
    elif num > 2:
        return -1
    elif num < 2:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while True:
            num = (low + high) / 2
            print num
            result = guess(num)
            if result == 0:
                return num
            elif result == -1:
                high = num
            elif result == 1:
                low = num + 1


s = Solution()
start = time.time()
print s.guessNumber(2)
print time.time() - start
