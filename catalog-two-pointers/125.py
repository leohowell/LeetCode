"""
https://leetcode.cn/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
"""
from operator import itemgetter


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = [item for item in s if 'a' <= item <= 'z']

        length = len(s)
        if length <= 1:
            return True

        for i in range(length//2):
            if s[i] != s[length-i-1]:
                return False

        return True
