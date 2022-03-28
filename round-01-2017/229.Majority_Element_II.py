# -*- coding: utf-8 -*-


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        count1 = 0
        count2 = 0
        candidate1 = 0
        candidate2 = 1

        for value in nums:
            if value == candidate1:
                count1 += 1
            elif value == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = value
                count1 = 1
            elif count2 == 0:
                candidate2 = value
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        return [
            n for n in (candidate1, candidate2)
            if nums.count(n) > len(nums) // 3
        ]

s = Solution()
print s.majorityElement([1,1,2,2,3])
