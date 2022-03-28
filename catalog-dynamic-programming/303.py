# -*- coding: utf-8 -*-


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.pre_process = [0]
        for i, n in enumerate(nums):
            self.pre_process.append(self.pre_process[-1] + n)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        return self.pre_process[j + 1] - self.pre_process[i]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
