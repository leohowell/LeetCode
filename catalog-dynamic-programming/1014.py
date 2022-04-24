
# 官方题解
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        max_left = values[0] + 0

        for j in range(1, len(values)):
            ans = max(ans, max_left + values[j] - j)
            max_left = max(max_left, values[j] + j)
        return ans


# 尝试改为动态规划版本
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0] * n
        dp_left = [0] * n
        dp_left[0] = values[0] + 0

        for j in range(n):
            dp[j] = max(dp[j-1], dp_left[j-1] + values[j] - j)
            dp_left[j] = max(dp_left[j-1], values[j] + j)
        return max(dp)


# 测试用例
# [5,7,4,10,4]
# [4,7,5,8]
# [1,3,5]
# [8,1,5,2,6]
# [1,2]
# [1,2,3,4,5,6,7,8,88,999,2]