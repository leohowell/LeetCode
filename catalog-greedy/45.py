# 45. 跳跃游戏 II
# https://leetcode-cn.com/problems/jump-game-ii/

# 我的解法
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        greed = [0] * n
        for i in range(n):
            greed[i] = i + nums[i]

        jump = 0
        n = n - 1
        while n > 0:
            for index, val in enumerate(greed):
                if val >= n:
                    n = index
                    jump += 1
                    break
        return jump