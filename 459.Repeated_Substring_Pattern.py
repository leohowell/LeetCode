# -*- coding: utf-8 -*-

"""
Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and
its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc"
twice.)
"""


class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        cand = str[0]

        for i, char in enumerate(str[1:len(str) / 2 + 1]):
            if char != cand[0]:
                cand += char
                continue
            else:
                try:
                    if self.is_repeat(str, cand):
                        return True
                except ValueError:
                    return False
                cand += char
                continue
        return False

    def is_repeat(self, string, sub):
        sub_len = len(sub)
        string_len = len(string)
        if string_len % sub_len != 0:
            return False

        for i in range(string_len / sub_len):
            start = i * sub_len
            if string[start: start + sub_len] != sub:
                if start >= string_len / 2:
                    raise ValueError
                return False
        return True
