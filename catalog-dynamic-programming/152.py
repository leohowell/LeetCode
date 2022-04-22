# 152. 乘积最大子数组
# https://leetcode-cn.com/problems/maximum-product-subarray/

# 我的解法
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        max_val = nums[0]
        point = 0
        for i in range(n):
            if nums[i] == 0:
                if not nums[point:i]:
                    point = i + 1
                    continue
                max_val = max(self.maxProductWithoutZero(nums[point:i]), max_val, 0)
                point = i + 1
        if point != n:
            max_val = max(self.maxProductWithoutZero(nums[point:n]), max_val)
        return max_val

    @staticmethod
    def maxProductWithoutZero(nums):
        # print(nums)
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        dp_max = [0] * n
        dp_max[0] = nums[0]

        dp_pos = dp[0] if dp[0] > 0 else None
        dp_neg = dp[0] if dp[0] < 0 else None

        for i in range(1, n):
            val = nums[i]
            mul = val * dp[i - 1]
            dp[i] = mul
            if mul > 0:
                if not dp_pos:
                    dp_pos = mul
                dp_max[i] = max(mul, val * dp_max[i - 1])
            else:
                if not dp_neg:
                    dp_neg = mul
                    dp_max[i] = val
                else:
                    dp_max[i] = mul / dp_neg

        return int(max(dp_max))
