from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
        # 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
        # 你从其中的一个加油站出发，开始时油箱为空。
        # 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，
        # 则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

        # 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # 输出: 3
        # 解释:
        # 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
        # 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
        # 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
        # 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
        # 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
        # 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
        # 因此，3 可为起始索引。

        # [1,2,3,4,5]
        # [3,4,5,1,2]
        # [-2, -2, -2, 3, 3]

        # [2, 3, 4]
        # [3, 4, 3]
        # [-1, -1, 1]

        # [1,2,3,4,5,1,11]
        # [3,4,5,1,2,11,1]
        # [-2, -2, -2, 3, 3, -10, 10]

        # [-1, 1, 1, 1, -1, -1, 1,-1]

        # [6,1,4,3,5]
        # [3,8,2,4,2]
        # [3,-7,2,-1,3]

        # 贪心算法
        index = -1
        all_cost = 0
        station_cnt = 0
        for i in range(len(gas) * 2):
            if station_cnt == len(gas):
                break

            i = i % len(gas)
            gap = gas[i] - cost[i]
            all_cost += gap

            if all_cost < 0:
                if gap < 0:
                    index = -1
                    all_cost = 0
                    station_cnt = 0
                    continue
                else:
                    index = i
                    all_cost = gap
                    station_cnt = 1
                    continue
            else:
                if index == -1:
                    index = i
                station_cnt += 1

        if station_cnt == len(gas):
            return index
        else:
            return -1


if __name__ == "__main__":
    Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3])
