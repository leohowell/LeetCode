# 977. 有序数组的平方
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/

# 我的解答
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_list = []
        right_list = []
        for index, num in enumerate(nums):
            if num >= 0:
                right_list.append(num)
            else:
                left_list.append(num)

        left_list = [item * -1 for item in left_list][::-1]

        result_list = []
        left = 0
        right = 0
        while left < len(left_list) and right < len(right_list):
            l = left_list[left]
            r = right_list[right]
            if l > r:
                result_list.append(r)
                right += 1
            else:
                result_list.append(l)
                left += 1
        if left < len(left_list):
            result_list += left_list[left:]
        if right < len(right_list):
            result_list += right_list[right:]
        return [item * item for item in result_list]


# 官方题解双指针
#
# 同样地，我们可以使用两个指针分别指向位置 00 和 n-1n−1，
# 每次比较两个指针对应的数，
# 选择较大的那个逆序放入答案并移动指针。
# 这种方法无需处理某一指针移动至边界的情况，读者可以仔细思考其精髓所在。
#
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            left_val = nums[left] * nums[left]
            right_val = nums[right] * nums[right]
            if left_val < right_val:
                result.append(right_val)
                right -= 1
            else:
                result.append(left_val)
                left += 1
        return result[::-1]
