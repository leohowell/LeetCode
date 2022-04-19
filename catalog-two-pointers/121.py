# 121. 买卖股票的最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

# 我的解答 基本同官方题解
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = prices[0], 0
        max_profit = 0

        for i in range(len(prices)):
            right = prices[i]

            if right <= left:  # 股价下降
                left = right
            else:  # 股价上升
                max_profit = max(right - left, max_profit)

        return max_profit
