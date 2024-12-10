from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        # 双指针

        left = 0
        right = len(height) - 1

        area = 0
        while left < right:
            x = right - left
            left_val = height[left]
            right_val = height[right]
            current = min(left_val, right_val) * x
            area = max(current, area)

            if left_val < right_val:
                left += 1
            else:
                right -= 1
        return area


if __name__ == "__main__":
    result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
