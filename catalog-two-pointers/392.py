# https://leetcode.cn/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 递归的做法, 拆分为子问题
        # return self.solution_recur(s, t)

        # 迭代的做法，无栈溢出
        return self.solution_iter(s, t)

        # 哈希的做法，大量判断的情况

    def solution_recur(self, s: str, t: str, s_index: int = 0, t_index: int = 0):
        if s_index == len(s):
            return True

        while t_index < len(t):
            if t[t_index] == s[s_index]:
                return self.solution_recur(s, t, s_index + 1, t_index + 1)
            else:
                t_index += 1
        return False

    def solution_iter(self, s, t):
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if t[t_index] == s[s_index]:
                s_index += 1
                t_index += 1
            else:
                t_index += 1

        return s_index == len(s)
