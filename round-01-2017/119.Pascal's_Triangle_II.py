# -*- coding: utf-8 -*-

import time


def triangles():
    L = [1]
    while True:
        time.sleep(0.5)
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        L = [1]
        for row in range(rowIndex):
            L.append(0)
            L = [L[i-1] + L[i] for i in range(len(L))]
        return L

s = Solution()
print s.getRow(3)
