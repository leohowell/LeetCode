#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except:
            return False
        else:
            return True
