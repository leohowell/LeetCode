# -*- coding: utf-8 -*-


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column = 0
        for index, item in enumerate(reversed(list(s))):
            column += self.mapping(item) * 26**index
        return column

    def mapping(self, char):
        return ord(char) - 64
