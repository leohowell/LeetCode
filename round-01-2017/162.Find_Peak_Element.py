# -*- coding: utf-8 -*-


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        elif length == 2:
            return 0 if nums[0] > nums[1] else 1
        elif nums[0] > nums[1]:
            return 0
        else:
            nums.append(-1)
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    return i
        return -1


s = Solution()
print s.findPeakElement([3, 2, 1])
