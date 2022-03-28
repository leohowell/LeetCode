#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for x in range(length):
            for y in range(x, length):
                if nums[x] + nums[y] == target and x != y:
                    return [x, y]
