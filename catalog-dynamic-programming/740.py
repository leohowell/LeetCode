# 740. 删除并获得点数
# https://leetcode-cn.com/problems/delete-and-earn/


# 我的解法
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_map = Counter(nums)

        keys = sorted(count_map.keys())
        n = len(keys)

        dp = [0] * (n+1)
        dp[0] = keys[0] * count_map[keys[0]]

        for i in range(1, n):
            val = keys[i]
            total = val*count_map[val]

            if val - keys[i-1] == 1:
                dp[i] = max(dp[i-2]+total, dp[i-1])
            else:
                dp[i] = dp[i-1] + total
        return dp[n-1]
