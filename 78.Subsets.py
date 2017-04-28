# -*- coding: utf-8 -*-


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.to_list(self.sub(nums)) + [[]]

    def sub(self, nums):
        if not nums:
            return [{}]

        if len(nums) == 1:
            return [{nums[0]: 1}]

        result = []
        n = nums[0]
        result.append({n: 1})
        sub = self.sub(nums[1:])
        for item in sub:
            if not self.is_exists2(item, result):
                result.append(item)

            cand = {}
            cand.update(item)
            cand[n] = cand.get(n, 0) + 1
            if not self.is_exists2(cand, result):
                result.append(cand)
        return result

    def is_exists2(self, target, result):
        for item in result:
            if item == target:
                return True
        return False

    def to_list(self, result):
        r = []
        for item in result:
            t = []
            for k, v in item.items():
                for i in range(v):
                    t.append(k)
            r.append(t)
        return r
