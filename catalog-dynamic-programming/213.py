# 213. 打家劫舍 II
# https://leetcode-cn.com/problems/house-robber-ii/

# 我的解法
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.solution(nums[1:]), self.solution(nums[:-1]))

    def solution(self, nums: List[int]) -> int:
        # 思考：尝试在数组最后添加nums[0], 然后使用dp求解
        n = len(nums)

        if not nums:
            return 0

        if n==1:
            return nums[0]

        # dp[i] 代表当前i的最优解
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
