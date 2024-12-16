from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 计算前缀和
        # 前缀和之差等于k
        output = 0
        hashmap = {0: 1}

        total = 0
        for i, num in enumerate(nums):
            total += num
            print(total, hashmap, total - k)
            output += hashmap.get(total - k, 0)

            if total in hashmap:
                hashmap[total] += 1
            else:
                hashmap[total] = 1

        return output


if __name__ == '__main__':
    # result = Solution().subarraySum([-1, -1, 1], 0)
    # print(result)

    result = Solution().subarraySum([1, 1, 1], 2)
    print(result)
