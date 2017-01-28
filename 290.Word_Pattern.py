# -*- coding: utf-8 -*-


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        _hash = {}
        str_list = str.split(' ')
        str_len = len(str_list)
        pattern_len = len(pattern)
        if str_len != pattern_len:
            return False
        for i in range(pattern_len):
            if pattern[i] not in _hash:
                if i >= str_len or str_list[i] in _hash.values():
                    return False
                _hash[pattern[i]] = str_list[i]
            else:
                if _hash[pattern[i]] == str_list[i]:
                    continue
                else:
                    return False
        else:
            return True


s = Solution()
print s.wordPattern("abba", "abba")
