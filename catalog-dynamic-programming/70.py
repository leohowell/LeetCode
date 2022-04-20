# 70. 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/

cache = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in cache:
            return cache[n]

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        cache[n] = res
        return res
