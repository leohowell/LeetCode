#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        temp = nums[0]
        index = 0
        for i in range(1, len(nums)):
            i -= index
            if nums[i] == temp:
                nums.pop(i)
                index += 1
            else:
                temp = nums[i]
        return len(nums)
