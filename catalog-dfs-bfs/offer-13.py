# 剑指 Offer 13. 机器人的运动范围
# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

# 参考了官方解答的方案名称
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 尝试使用广度优先搜索解题
        used = set()

        next_round = {(0, 0), }
        while next_round:
            used |= next_round
            cand = set()
            for i, j in next_round:
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if m > x >= 0 and n > y >= 0 \
                            and (x, y) not in used \
                            and (x // 10 + x % 10 + y // 10 + y % 10) <= k:
                        cand.add((x, y))
            next_round = cand
        return len(used)
