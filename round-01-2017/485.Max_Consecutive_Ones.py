# -*- coding: utf-8 -*-


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_length = 0
        current_length = 0
        nums.append(0)
        for num in nums:
            if not 1 ^ num:
                current_length += 1
                continue
            else:
                if current_length > max_length:
                    max_length = current_length
                current_length = 0
        return max_length


s = Solution()
print s.findMaxConsecutiveOnes([0,0,0])
