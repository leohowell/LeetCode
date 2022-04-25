# 22. 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/

# 我的解法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1 ()
        # 2 ()() (())
        # 3 ()()() (())() ()(()) (()()) ((()))
        # 4 (())(())
        # 状态转移方程
        # (())()
        # (()())()  ((()))() (())(())
        # dp[i] = dp[i-i]
        dp = [0] * n
        dp[0] = {"()", }

        def add(val):
            cand = {f"{val}()", f"(){val}", f"({val})"}
            for index, char in enumerate(val):
                if char == "(":
                    cand.add(f"{val[:index+1]}(){val[index+1:]}")
            return cand

        for i in range(1, n):
            values = set()
            for item in dp[i-1]:
                values |= add(item)
            dp[i] = values

        return list(dp[n-1])
