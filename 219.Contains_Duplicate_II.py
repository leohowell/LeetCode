# -*- coding: utf-8 -*-


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        _hash = {}
        for i, n in enumerate(nums):
            if n not in _hash:
                _hash[n] = i
            else:
                if i - _hash[n] <= k:
                    return True
                _hash[n] = i
        else:
            return False
