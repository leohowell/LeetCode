# 215. 数组中的第K个最大元素
# https://leetcode.cn/problems/kth-largest-element-in-an-array/


# 我的解法
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 尝试使用快排的方式解决问题

        stake = nums[0]

        if len(nums) == 1 and k == 1:
            return stake

        left = []
        right = []
        for num in nums[1:]:
            if num >= stake:
                right.append(num)
            else:
                left.append(num)

        if len(right) + 1 == k:
            return stake
        elif len(right) >= k:
            return self.findKthLargest(right, k)
        else:
            k = k - len(right) - 1
            return self.findKthLargest(left, k)
