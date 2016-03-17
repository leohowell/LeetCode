# -*- coding: utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(digits) + 2):
            if i > len(digits):
                digits.insert(0, 0)
            if digits[-i] + 1 > 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                break
        return digits
