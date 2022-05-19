# 338. 比特位计数
# https://leetcode.cn/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(x).count("1") for x in range(n+1)]
