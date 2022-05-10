# 122. 买卖股票的最佳时机 II
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

# 我的解法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态转移方程
        # 思考f(n)与f(n-1)的关系
        # 假设f(n-1) 全局最优
        # f(n)

        n = len(prices)
        dp = [] * n  # (start, end, profit)

        # dp[0]
        dp.append((0, 0, 0))

        max_profit = 0

        for i in range(1, n):
            val = prices[i]
            last_val = prices[i - 1]

            if val <= last_val:
                dp.append(dp[-1])
            else:
                last_start, last_end, last_profit = dp[-1]
                if last_end == i - 1:
                    profit = val - prices[last_start]
                    dp.append((last_start, i, profit))
                    max_profit += profit - last_profit
                else:
                    profit = val - last_val
                    max_span_profit = val - prices[last_start]
                    if max_span_profit > profit + last_profit:
                        dp.append((last_start, i, max_span_profit))
                        max_profit += max_span_profit - last_profit
                    else:
                        dp.append((i - 1, i, profit))
                        max_profit += profit
        # for i, val in enumerate(dp):
        #     print(i, "===", val)
        return max_profit


# [7,1,5,3,6,4]
# [1,2,3,4,5]
# [7,6,4,3,1]
# [1]
# [1,100]
# [100,1]
# [1,99,98,1]
# [1,2,3,4,3,2,1]
