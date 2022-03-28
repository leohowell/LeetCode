#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = - int((str(x)[1:])[::-1])
        else:
            x = int((str(x))[::-1])

        if not -2147483647 < x < 2147483647:
            return 0
        else:
            return x
