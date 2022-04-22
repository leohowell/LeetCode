# 没做对，看了官网题解
# 分为两种情况
# 1. 最大值在中间 = 最大连续最大和
# 2. 最大值包含两端 = 总和 - 最大连续最小和


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans1 = self.maxSubArray(nums)
        ans2 = sum(nums) - self.minSubArray(nums[1:-1])
        print(ans1, ans2)
        return max(ans1, ans2)

    @staticmethod
    def maxSubArray(nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            val = nums[i]
            dp[i] = max(dp[i - 1] + val, val)

        # print("max ", dp)
        return max(dp)

    @staticmethod
    def minSubArray(nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            val = nums[i]
            dp[i] = min(dp[i - 1] + val, val)

        # print("min ", dp)
        return min(dp)
