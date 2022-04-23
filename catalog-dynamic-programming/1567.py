# 1567. 乘积为正数的最长子数组长度
# https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product/

# 参考了官方题解
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)

        dp_pos = [0] * n
        dp_neg = [0] * n

        v0 = nums[0]
        if v0 > 0:
            dp_pos[0] = 1
        elif v0 < 0:
            dp_neg[0] = 1

        for i in range(1, n):
            val = nums[i]
            if val > 0:
                dp_pos[i] = dp_pos[i-1] + 1
                if dp_neg[i - 1] != 0:
                    dp_neg[i] = dp_neg[i-1] + 1
            elif val < 0:
                dp_neg[i] = dp_pos[i-1] + 1
                if dp_neg[i-1] == 0:
                    dp_pos[i] = 0
                else:
                    dp_pos[i] = dp_neg[i-1] + 1
            else:
                pass
        # print(dp_pos, dp_neg)
        return max(dp_pos)


# [0,-7,-10,-7,21,20,-12,-34,26,2]
# [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
# [-1,2]
# [1,2,3,5,-6,4,0,10]
# [-16,0,-5,2,2,-13,11,8]
# [1,-2,-3,4]
# [0,1,-2,-3,-4]
# [-1,-2,-3,0,1]
# [0]
# [1]
# [1,2]
# [0,0,0,0,1,2,3,4,5,6,7,8,0,0,-999,999]
