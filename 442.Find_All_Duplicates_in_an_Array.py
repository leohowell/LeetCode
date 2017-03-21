# -*- coding: utf-8 -*-


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = {}
        for n in nums:
            tmp[n] = tmp.get(n, 0) + 1
        return [k for k, v in tmp.items() if v == 2]


s = Solution()
print s.findDuplicates([4,3,2,7,8,2,3,1])
print s.findDuplicates([1,1,1])

