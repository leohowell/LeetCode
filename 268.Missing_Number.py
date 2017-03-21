# -*- coding: utf-8 -*-


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) + 1) * len(nums) / 2 - sum(nums)

s = Solution()
print s.missingNumber([0, 1, 2,3,4,6,7,8,9])