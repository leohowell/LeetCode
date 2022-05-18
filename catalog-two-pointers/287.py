# 287. 寻找重复数
# https://leetcode.cn/problems/find-the-duplicate-number/

from typing import List


# 参考题解
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针

        fast, slow, start = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while True:
            slow = nums[slow]
            start = nums[start]
            if slow == start:
                return start
