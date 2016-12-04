# -*- coding: utf-8 -*-


"""
Given a string which consists of lowercase or uppercase letters, find
the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        palind = 0
        fix = 0
        for char in s:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
        for char, count in table.items():
            if count >= 2:
                if count % 2 == 0:
                    palind += count
                else:
                    palind += count - 1
                    fix = fix if fix else 1
            else:
                fix = fix if fix else 1
        palind += fix
        return palind
