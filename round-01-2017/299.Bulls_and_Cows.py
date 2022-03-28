# -*- coding: utf-8 -*-


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = []
        B = 0

        l = len(secret)
        guess = list(guess)
        for i in range(l):
            if secret[i] == guess[i]:
                A.append(i)
                guess[i] = '-'

        for i in range(l):
            if i in A:
                continue
            if secret[i] in guess:
                guess.remove(secret[i])
                B += 1
        return '%dA%dB' % (len(A), B)

s = Solution()
print s.getHint('1123', '0111')






