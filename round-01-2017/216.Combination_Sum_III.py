# -*- coding: utf-8 -*-


class Solution(object):
    RESULT = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.RESULT = []
        if n < sum(range(1, k+1)):
            return []
        self.foo(k, n, set(range(1, 10)), 0)

        return self.RESULT

    def foo(self, k, n, pool, last):
        if k == 1:
            if n <= last:
                return
            if n in pool:
                self.RESULT.append([x for x in range(1, 10) if x not in pool] + [n])
                return True
            else:
                return False
        else:
            for i in pool:
                if i <= last:
                    continue
                pool.remove(i)
                self.foo(k-1, n-i, pool, i)
                pool.add(i)


s = Solution()
print s.combinationSum3(9, 45)
