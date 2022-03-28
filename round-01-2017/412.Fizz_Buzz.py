# -*- coding: utf-8 -*-


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i) for i in range(1, n + 1)]
