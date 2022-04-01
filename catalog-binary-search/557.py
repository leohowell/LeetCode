# 557. 反转字符串中的单词 III
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

# 我的解法
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([item[::-1] for item in s.split(" ")])
