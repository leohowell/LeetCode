# -*- coding: utf-8 -*-


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        if n == 1:
            return string
        for i in range(n-1):
            string = self.translate(string)
        return string

    def translate(self, string):
        def process_stack(stack):
            l = len(stack)
            return '%d%s' % (l, stack[0])

        stack = []
        result = []
        for i in string:
            if not stack or i == stack[-1]:
                stack.append(i)
            else:
                result.append(process_stack(stack))
                stack = [i]
        if stack:
            result.append(process_stack(stack))
        return ''.join(result)




s = Solution()
print s.translate('312211')
print s.countAndSay(6)
