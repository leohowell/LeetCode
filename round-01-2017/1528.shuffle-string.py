class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [''] * len(s)
        for i, item in enumerate(indices):
            res[item] = s[i]
        return ''.join(res)
