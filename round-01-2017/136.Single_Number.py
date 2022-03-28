# -*- coding: utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in nums[1:]:
            nums[0] ^= item
        return nums[0]
