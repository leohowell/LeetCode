# -*- coding: utf-8 -*-


"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []

        start = None
        last = None
        for n in nums:
            if start is None:
                start = n
            if last is None:
                last = n
                continue

            if n - last == 1:
                last = n
                continue
            else:
                if last == start:
                    result.append(str(last))
                else:
                    result.append('%s->%s' % (start, last))
                start = n
                last = n

        if last is None or start == last:
            result.append(str(start))
        else:
            result.append('%s->%s' % (start, last))
        return result


s = Solution()
print s.summaryRanges([0,5,9])
