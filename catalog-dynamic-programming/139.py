# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/
# 关键点：当前结果与下一结果之间的关系
# 提示：取最后一个字母构建hash


from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashed = {}
        for word in sorted(wordDict, key=lambda x: len(x), reverse=True):
            values = hashed.setdefault(word[-1], [])
            values.append(word)
        print(hashed)

        # 尝试使用动态规划
        n = len(s)
        dp = [False] * n

        for i in range(n):
            val = s[i]

            if val not in hashed:
                dp[i] = False
                continue

            for word in hashed[val]:
                length = len(word)
                if length == 1 and dp[i-1]:
                    dp[i] = True
                    break
                elif length == i + 1:
                    if s[:i+1] == word:
                        dp[i] = True
                        break
                elif length < i + 1:
                    sep_index = i - length
                    if dp[sep_index] and s[sep_index+1:i+1] == word:
                        dp[i] = True
                        break

        print(dp)
        return dp[-1]


# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# "leetcode"
# ["leet","code"]
# "applepenapple"
# ["apple", "pen"]
# "catsandog"
# ["cats", "dog", "sand", "and", "cat"]
# "abcd"
# ["a", "b", "c", "d"]
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# "abcd"
# ["a","abc","b","cd"]

input_s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
input_words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

print(Solution().wordBreak(input_s, input_words))
