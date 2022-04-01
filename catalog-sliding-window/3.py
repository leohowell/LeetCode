# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# 我的解答1 勉强通过,需优化
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right = 0, 1
        max_offset = 0
        while right < len(s):
            for index, val in enumerate(s[left:right]):
                if val == s[right]:
                    left += index + 1
                    right = left+1
                    break
            else:
                right += 1
                max_offset = max(max_offset, right - left)
        return max(max_offset, right - left)

# 我的解答 缓存优化版
