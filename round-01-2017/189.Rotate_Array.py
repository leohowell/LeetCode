# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())


s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)
