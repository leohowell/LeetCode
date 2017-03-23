# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        last = None
        for i, n in enumerate(numbers, start=1):
            if n == last:
                continue
            last = n
            index1 = i
            index2 = self.binary_search(numbers[i:], target-n)
            if index2 is not None:
                return [index1, index2 + i + 1]
        return []

    def binary_search(self, nums, target):
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid
            elif nums[mid] == target:
                return mid
            else:
                low = mid + 1

        if low < 1 or low >= len(nums):
            return None
        elif nums[low] != target:
            return None
        return low


s = Solution()
print s.twoSum([1,2,3,4,4,9,56,90], 8)
