from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
        # 使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
        last_value = nums[0]
        last_cnt = 1
        offset = 0
        for i in range(1, len(nums)):
            i = i - offset
            num = nums[i]
            if num == last_value:
                last_cnt += 1
                if last_cnt >= 3:
                    nums.pop(i)
                    offset += 1
            else:
                last_value = nums[i]
                last_cnt = 1
        return len(nums)
