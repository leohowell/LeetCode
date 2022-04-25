# 131. 分割回文串
# https://leetcode-cn.com/problems/palindrome-partitioning/


# 我的解法
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # aabaa
        # a a b a a
        # aa b aa
        # aabaa
        # a aba a
        # a => a
        # aa => a a | aa
        # aab => a a b | aa b
        # aaba => a a b a | aa b a | a aba
        # aabaa => a a b a a | aa b a a | aa b aa| a aba a | aabaa
        # aabaab => a a b a a b | aa b a a b| aa b aa b| a aba a b| aabaa b
        # aabaaba => a a b a a b a| aa b a a b a| aa b aa b a| a aba a b a| aabaa b a
        #         => a a b a a bb| aa b a a bb| aa b aa bb| a aba a bb| aabaa bb
        n = len(s)
        dp = [[] for _ in range(n)]
        dp[0] = [[s[0]]]

        for i in range(1, n):
            ans = []
            val = s[i]
            for item in dp[i - 1]:
                ans.append(item + [val])
                if item[-1] == val:
                    ans.append(item[:-1] + [f"{val}{val}"])
                if len(item) >= 2 and item[-2] == val:
                    ans.append(item[:-2] + [f"{val}{item[-1]}{val}"])
            dp[i] = ans

        # for index, val in enumerate(dp):
        #     print(index, "==", val)

        return dp[n - 1]
