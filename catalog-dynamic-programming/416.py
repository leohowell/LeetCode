# 416. 分割等和子集
# https://leetcode-cn.com/problems/partition-equal-subset-sum/

# 我的解法
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1 5 11 5
        # 1 => false
        # 1 5 => false 1|5 need 4
        # 1 5 11 => false 11 != 4 => neg 1|16=15 12|5=7 6|11=5
        # 1 5 11 6 => 6|17
        n = len(nums)
        if n == 1:
            return False
        if n == 2:
            return nums[0] == nums[1]

        dp = [[] for _ in range(n)]
        dp[1] = [[nums[0], nums[1]]]

        for i in range(2, n):
            val = nums[i]

            values = set()
            for left, right in dp[i - 1]:
                if abs(left - right) == val or abs(left + right - val) == 0:
                    if i == n - 1:
                        return True

                if left + val < right:
                    values.add((left + val, right))
                else:
                    values.add((right, left + val))

                if left < right + val:
                    values.add((left, right + val))
                else:
                    values.add((right + val, left))

                if val < left + right:
                    values.add((val, left + right))
                else:
                    values.add((left + right, val))

            dp[i] = values

        # for index, val in enumerate(dp):
        #     print(index, '===', val)
        return False
