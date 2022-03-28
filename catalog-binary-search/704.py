# 704. 二分查找
# https://leetcode-cn.com/problems/binary-search/


# 我的解法
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums)
        middle = (right + left) // 2
        while True:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle
                middle = (right + left) // 2
                if middle == left:
                    return -1
            else:
                right = middle
                middle = (right + left) // 2
                if middle == right:
                    return -1


# 官方题解
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return -1
