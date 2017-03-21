# -*- coding: utf-8 -*-


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        l = len(nums)

        for i in range(l):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(l-1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output

s = Solution()
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
