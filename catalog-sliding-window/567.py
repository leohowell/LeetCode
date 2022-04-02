# 567. 字符串的排列
# https://leetcode-cn.com/problems/permutation-in-string/

# 我的解答
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2

        left, right = 0, 0
        chars = {}
        for char in s1:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

        while left + len(s1) <= len(s2):
            left_val = s2[left]
            right = left + len(s1) - 1
            right_val = s2[right]
            if left_val in chars \
                    and right_val in chars \
                    and (left_val != right_val or (chars[left_val] >= 2)):

                new_chars = {}
                for char in s2[left:left + len(s1)]:
                    if char in new_chars:
                        new_chars[char] += 1
                    else:
                        new_chars[char] = 1

                if len(chars) != len(new_chars):
                    left += 1
                    continue

                for k, v in chars.items():
                    if new_chars.get(k) != v:
                        left += 1
                        break
                else:
                    return True
            else:
                left += 1

        return False


# 题解优化版
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2

        left, right = 0, 0
        chars = {}
        for char in s1:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

        # 当前窗口各字符数量统计
        new_chars = {}

        while left < len(s2):
            print(f"left: {left}, val: {s2[left]}")

            if not new_chars:
                for char in s2[left:left + len(s1)]:
                    if char in new_chars:
                        new_chars[char] += 1
                    else:
                        new_chars[char] = 1
                left += len(s1) - 1
            else:
                char = s2[left]
                pop_char = s2[left - len(s1)]
                if char not in new_chars:
                    new_chars[char] = 1
                else:
                    new_chars[char] += 1
                if pop_char in new_chars:
                    new_chars[pop_char] -= 1
                    if new_chars[pop_char] == 0:
                        del new_chars[pop_char]

            # 判断是否是子串排列
            for k, v in chars.items():
                if new_chars.get(k) != v:
                    left += 1
                    break
            else:
                return True

        return False

# 测试用例
"""
"abcd"
"abbdabbdabbdabbdabbdabbdabbdabbdabbdabbdabbdabbdabbdabbd"
"ljk"
"abcdefghijkl"
"ab"
"eidbaooo"
"abb"
"eidbbaooo"
"a"
"a"
"bbbbbbbbbbbb"
"aaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
"""