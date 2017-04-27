# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = 1
        last = nums[0]
        two = False
        fix = 0

        for i in range(len(nums[1:])):
            real_index = i+1-fix
            n = nums[real_index]
            if not n ^ last:
                if not two:
                    two = True
                    length += 1
                else:
                    del nums[real_index]
                    fix += 1
            else:
                length += 1
                two = False
            last = n
        return length


s = Solution()
print s.removeDuplicates([1, 1, 1, 2, 2, 3])
print s.removeDuplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                          2, 2, 2, 2, 2, 2, 2, 2, 2, 3])
print s.removeDuplicates([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
