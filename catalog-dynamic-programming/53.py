# -*- coding: utf-8 -*-


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_num = nums[0]
        cur_num = nums[0]
        for n in nums[1:]:
            cur_num = max(n, n + cur_num)
            max_num = max(cur_num, max_num)
        return max_num


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# 动态规划 我的解法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] i代表当前最优解
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            # 状态转移方程
            val = nums[i]
            dp[i] = max(dp[i - 1] + val, val)
        return max(dp)
