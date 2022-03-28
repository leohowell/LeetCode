# -*- coding: utf-8 -*-


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                s = n + 1
                while s in nums:
                    s += 1
                best = max(best, s - n)
        return best

s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))

