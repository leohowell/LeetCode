# 322. 零钱兑换
# https://leetcode-cn.com/problems/coin-change/

# 尝试使用深度优先解决题目

from typing import List


# 尝试使用深度优先遍历, Recursion Error
def solution(coins: List[int], amount: int):
    coins = [coin for coin in coins if coin <= amount]
    coins = sorted(coins)

    max_coin_cnt = amount // coins[-1]
    if amount % coins[-1] == 0:
        return max_coin_cnt

    for i in range(max_coin_cnt, -1, -1):
        new_amount = amount - i * coins[-1]
        res = solution(coins, new_amount)
        if res != -1:
            return i + res

    return -1


# 尝试使用动态规划(思路正确，提交错误，又看了答案解决的)
def solution2(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    coins = [coin for coin in coins if coin <= amount]
    if not coins:
        return -1

    coins = sorted(coins)
    coin_set = set(coins)

    dp = [0] * (amount+1)

    for i in range(1, amount+1):
        if i in coin_set:
            dp[i] = 1
            continue

        current_max = -1
        for coin in coins:
            left_index = i - coin
            if left_index >= 0 and dp[left_index] != -1:
                if current_max == -1:
                    current_max = dp[left_index] + 1
                else:
                    current_max = min(dp[left_index] + 1, current_max)
        dp[i] = current_max

    return dp[amount]


print(solution2([186, 419, 83, 408], 6249))


# [1,2,5]
# 11
# [2]
# 3
# [1]
# 0
# [1,2,5]
# 9998
# [3,4]
# 9
# [3,4]
# 10
# [3,4]
# 11
# [1,999]
# 998
# [400,500]
# 800
# [1]
# 1
# [2]
# 1
# [186,419,83,408]
# 6249
