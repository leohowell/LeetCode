# 120. 三角形最小路径和
# https://leetcode-cn.com/problems/triangle/

# 参考了官方题解
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp[i][j]为到达最底层i,j位置的最小路径和
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        if n == 1:
            return dp[0][0]

        dp[1][0] = triangle[1][0] + dp[0][0]
        dp[1][1] = triangle[1][1] + dp[0][0]

        for i in range(2, n):
            items = triangle[i]
            for j in range(i + 1):
                # 状态转移方程
                if j == 0:
                    dp[i][j] = items[j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = items[j] + dp[i-1][j-1]
                else:
                    dp[i][j] = items[j] + min(dp[i-1][j], dp[i-1][j-1])
        return min(dp[n-1])
