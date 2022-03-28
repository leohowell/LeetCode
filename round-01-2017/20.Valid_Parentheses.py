# -*- coding: utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or abs(ord(char) - ord(stack.pop())) > 2:
                    return False
        if stack:
            return False
        return True


s = Solution()
print s.isValid('{)')
