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


def solution(n):
    # dp为到第n阶所需的最小次数
    dp = [0] * n + 1
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
