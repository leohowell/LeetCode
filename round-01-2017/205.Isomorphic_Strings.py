# -*- coding: utf-8 -*-


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = {}
        T = {}
        for i in range(len(s)):
            if s[i] in S:
                S[s[i]] += i+1
            else:
                S[s[i]] = i+1
            if t[i] in T:
                T[t[i]] += i+1
            else:
                T[t[i]] = i+1

            if not S[s[i]] == T[t[i]]:
                return False
        else:
            return True


s = Solution()
print s.isIsomorphic('aa', 'ab')
