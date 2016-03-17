class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_len = min([len(item) for item in strs])
        if min_len == 0:
            return ''
          
        total = len(strs)
        min_exist = 0
        for i in range(min_len):
            print i
            if not self.is_equal(strs, i, total):
                min_exist = 1
                break
        return strs[0][:i + 1-min_exist]


    @classmethod
    def is_equal(cls, strs, index, items):
        return len(set([item[index] for item in strs])) == 1

