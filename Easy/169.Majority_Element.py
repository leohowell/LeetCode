# -*- coding: utf-8 -*-


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stats = {}
        for item in nums:
            if item not in stats:
                stats[item] = 1
            else:
                stats[item] += 1

        restats = dict((v, k) for (k, v) in stats.items())
        return restats[max(restats.keys())]
