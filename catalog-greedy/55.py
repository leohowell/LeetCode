# 55. 跳跃游戏
# https://leetcode-cn.com/problems/jump-game/

# 我的解法 非动态规划
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] == 0:
            return False if n != 1 else True

        last_0 = 0
        i = n
        while i > 0:
            i -= 1
            val = nums[i]
            # print("val:", val)
            if val == 0:
                j = i
                t = 0
                while j > 0:
                    j -= 1
                    t += 1
                    if nums[j] > t or (i == (n - 1) and nums[j] >= t):
                        i = j
                        # print("i = ", i)
                        break
                else:
                    return False
            else:
                continue
        return True


# 测试用例
# [3,0,0,0]
# [1,0,4,1,4,3,0,4]
# [0,2,3]
# [2,3,1,1,4]
# [3,2,1,0,4]
# [0]
# [1,0]
# [6,5,4,3,2,1,0,1,1,1,1]
# [7,5,4,3,2,1,0,1,1,1,1]

# 官方题解 贪心
# 维护一个数组[] 该数组表示可以到达的最远位置
def solution(nums):
    n = len(nums)
    max_pos = 0

    for i in range(n):
        val = nums[i]
        if max_pos < i:
            return False
        max_pos = max(i + val, max_pos)
    return True
