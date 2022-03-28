# -*- coding: utf-8 -*-


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) / 2
            if target < nums[mid]:
                high = mid
            elif target == nums[mid]:
                return mid
            else:
                low = mid + 1
        return low
