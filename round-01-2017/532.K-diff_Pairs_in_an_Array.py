# -*- coding: utf-8 -*-


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k == 0:
            hash_ = {}
            for item in nums:
                hash_[item] = (hash_.get(item) is not None) + 1
            return len([key for key in hash_ if hash_[key] >= 2])
        else:
            return len(set(nums) & set([n + k for n in nums]))


s = Solution()
print s.findPairs([3, 1, 4, 1, 5], 2)
print s.findPairs([1, 2, 3, 4, 5], 1)
print s.findPairs([1, 3, 1, 5, 4], 0)
