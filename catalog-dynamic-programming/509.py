# 509. 斐波那契数
# https://leetcode-cn.com/problems/fibonacci-number/

# 自顶向下解法
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        # 动态规划dp[] 保存到最后一个数字的和
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
