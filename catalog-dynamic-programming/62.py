# 62. 不同路径
# https://leetcode-cn.com/problems/unique-paths/


# 我的解法
cache = {}


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m x n
        # f(m, n) = f(m-1, n) + f(m, n-1)
        # f(1,1) = 0
        # f(2, 1) = 1
        # f(1, 2) = 1
        # f(2, 2) = f(2, 1) + f(1, 2) = 1 + 1 = 2
        # f(3, 2) = f(2, 2) + f(3, 1) = 2 + 2 = 4
        if m == 1 or n == 1:
            return 1
        if (m, n) in cache:
            return cache[(m, n)]
        else:
            res = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
            cache[(m, n)] = res
            return res


# 1
# 1
# 2
# 2
# 1
# 2
# 1
# 99
# 3
# 7
# 3
# 2
# 7
# 3
# 3
# 3
# 10
# 10
# 15
# 14
