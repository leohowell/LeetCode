# -*- coding: utf-8 -*-


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
