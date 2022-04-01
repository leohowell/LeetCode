# 283. 移动零
# https://leetcode-cn.com/problems/move-zeroes/

# 我的解答
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = 0
        right = len(nums)
        while length < right:
            if nums[length] == 0:
                nums.pop(length)
                nums.append(0)
                right -= 1
            else:
                length += 1
