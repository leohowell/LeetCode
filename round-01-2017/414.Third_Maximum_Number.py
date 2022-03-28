# -*- coding: utf-8 -*-


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = nums[0]
        two = None
        thr = None

        for x in nums[1:]:
            if x == one:
                continue
            elif x > one:
                one, two, thr = x, one, two
            elif not two:
                two = x
            elif x == two:
                continue
            elif x > two:
                two, thr = x, two
            elif not thr:
                thr = x
            elif x == thr:
                continue
            elif x > thr:
                thr = x

        return thr if thr is not None else one


b = Solution()
print b.thirdMax([3,3,4,3,4,3,0,3,3])
