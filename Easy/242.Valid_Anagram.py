# -*- coding: utf-8 -*-


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        list_t = list(t)
        for item in s:
            try:
                list_t.remove(item)
            except:
                return False
        return not bool(list_t)
