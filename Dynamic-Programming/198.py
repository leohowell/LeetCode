# -*- coding: utf-8 -*-


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        a = 0
        b = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                a = max(a+n, b)
            else:
                b = max(b+n, a)

        return max(a, b)


print(Solution().rob([6, 11, 2, 17, 16, 0, 9, 5, 9, 3]))
print(Solution().rob([100, 100000, 10, 1000]))
