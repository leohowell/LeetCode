# -*- coding: utf-8 -*-


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = []

        def wapper(n):
            if n in temp:
                return False
            if n != 1:
                temp.append(n)
                return wapper(sum([int(x) * int(x) for x in list(str(n))]))
            else:
                return True
        return wapper(n)
