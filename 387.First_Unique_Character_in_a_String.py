# -*- coding: utf-8 -*-

"""
Given a string, find the first non-repeating character in it
and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = {}
        dup = set()
        index = []
        for i, char in enumerate(s):
            if char in dup:
                continue
            if char not in unique:
                unique[char] = i
                index.append(i)
            else:
                dup.add(char)
                index.remove(unique[char])
                del unique[char]
        return index[0] if index else -1
