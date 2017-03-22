# -*- coding: utf-8 -*-


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        start = 0
        max_length = len(nums) + 1
        min_length = max_length

        for i, n in enumerate(nums, start=1):
            total += n
            while total >= s:
                min_length = min(min_length, i-start)
                total -= nums[start]
                start += 1
        return min_length if min_length != max_length else 0


s = Solution()
print s.minSubArrayLen(3, [1, 1])
