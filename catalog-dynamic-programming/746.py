# 746. 使用最小花费爬楼梯
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/

# 使用动态规划，数组dp[] dp[i]代表到达i点的最小花费
# [1,100,1,1,1,100,1,1,100,1]

def solution(cost):
    n = len(cost)
    # dp[i]代表到达i点的最小花费
    dp = [0] * (n + 1)

    for i in range(2, n+1):
        dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
    print(dp[-1])
    return dp[-1]


solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
solution([10, 15, 20])
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4])
