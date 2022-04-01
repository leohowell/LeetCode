# 189. 轮转数组
# https://leetcode-cn.com/problems/rotate-array/

# 我的解答 空间复杂度O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for item in list(nums[-k:][::-1]):
            nums.insert(0, item)
            nums.pop()


# 官方题解 待补充
