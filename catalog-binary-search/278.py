# 278. 第一个错误的版本
# https://leetcode-cn.com/problems/first-bad-version/

# 我的解答
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1

        low, high = 1, n
        last_mid = None
        last_result = None
        while low <= high:
            mid = (high - low) // 2 + low

            result = isBadVersion(mid)

            if result != last_result and abs(mid - last_mid) == 1:
                return max(mid, last_mid)

            last_mid = mid
            last_result = result

            # true
            if result:
                high = mid - 1
            else:
                low = mid + 1

            if low == mid:
                return mid
            if high == mid:
                return low


# 官方题解
class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid  # 答案在区间[low, mid]
            else:
                low = mid + 1  # 答案在区间[mid+1, high]中
        return low
