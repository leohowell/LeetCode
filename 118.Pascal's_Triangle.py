# -*- coding: utf-8 -*-


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def triangle():
            L = [1]
            while True:
                yield L
                S = [1]
                for i in range(1, len(L)):
                    S.append(L[i-1] + L[i])
                S.append(1)
                L = S

        tri = triangle()
        return [tri.next() for x in range(numRows)]


s = Solution()
print s.generate(5)
