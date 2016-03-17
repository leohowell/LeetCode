#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.strip().split(' ')
        return len(list_s[-1])
