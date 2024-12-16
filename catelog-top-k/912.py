# 912. 排序数组
# https://leetcode.cn/problems/sort-an-array/

from typing import List


# 我的解法，答案正确，超时
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return nums
        elif n == 1:
            return nums
        elif n == 2:
            if nums[0] > nums[1]:
                return [nums[1], nums[0]]
            else:
                return nums

        stake = nums[0]

        left = []
        right = []
        for num in nums[1:]:
            if num >= stake:
                right.append(num)
            else:
                left.append(num)
        return self.sortArray(left) + [stake] + self.sortArray(right)


# 不要使用递归 通过 8864 ms
def solution(nums):
    stack = [(0, len(nums))]

    while stack:
        left, right = stack.pop()
        middle = random.randint(left, right-1)
        origin_middle = middle

        stake = nums[middle]

        for i in range(origin_middle, right):
            val = nums[i]
            if val < stake:
                nums = exchange(nums, middle, i)
                middle += 1

        for i in range(origin_middle, left-1, -1):
            val = nums[i]
            if val > stake:
                nums = exchange2(nums, i, middle)
                middle -= 1

        if middle + 1 < right:
            stack.append((middle + 1, right))
        if left < middle - 1:
            stack.append((left, middle))
    return nums


def exchange(nums, a, b):
    val_b = nums[b]
    nums[a+1:b+1] = nums[a:b]
    nums[a] = val_b
    return nums


def exchange2(nums, a, b):
    val_a = nums[a]
    nums[a:b] = nums[a+1:b+1]
    nums[b] = val_a
    return nums


# 归并排序
def solution2(nums):
    pass


import random
import time

x = list(range(50000))
random.shuffle(x)

start = time.perf_counter()
print(solution(x)[:100])
# print(Solution().sortArray(x))
cost = int((time.perf_counter() - start) * 1000)
print(f"{cost}ms")

# x = list(range(50000))