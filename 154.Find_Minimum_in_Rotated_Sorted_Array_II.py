# -*- coding: utf-8 -*-


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        last = nums[0]
        for n in nums[1:]:
            if n < last:
                return n
            last = n
        else:
            return nums[0]


s = Solution()
print s.findMin([4, 5, 6, 7, 0, 0, 1, 2])
print s.findMin([1])
print s.findMin([1, 2, 3])
print s.findMin([2, 1, 1])
