# -*- coding: utf-8 -*-


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        a = 0
        b = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                a = max(a+n, b)
            else:
                b = max(b+n, a)

        return max(a, b)


print(Solution().rob([6, 11, 2, 17, 16, 0, 9, 5, 9, 3]))
print(Solution().rob([100, 100000, 10, 1000]))


# 动态规划版本
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # dp[] 代表当前房间数能够偷窃到的最大金额
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # 状态转移方程
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
