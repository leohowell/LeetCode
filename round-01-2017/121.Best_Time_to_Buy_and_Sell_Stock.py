# -*- coding: utf-8 -*-

"""
Say you have an array for which the i element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm
to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max = prices[0]
        min = prices[0]
        profit = 0
        for i, price in enumerate(prices[1:]):
            if price < min:
                min = price
                max = price
                continue
            if price > max:
                max = price
                new_profit = max - min
                if new_profit > profit:
                    profit = new_profit
        return profit
