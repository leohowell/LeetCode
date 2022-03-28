# 找出其中不含有重复字符的最长子串的长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        cache = {}
        length = len(s)

        left = 0

        for i in range(length):
            char = s[i]

            # 如果前序已有该字符
            if char in cache:
                # 获取字符索引
                index = cache[char]
                # 如果重复字符索引大于等于左指针
                cache[char] = i
                if index >= left:
                    left = index + 1
                    # print(f"left: {left}, max: {max_len}: char: {char}")
                # 如果重复字符的索引小于左指针
                else:
                    max_len = max(i - left + 1, max_len)
                    # print(f"left: {left}, max: {max_len}: char: {char}")
                    continue
            # 如果前序没有该字符
            else:
                cache[char] = i
                max_len = max(i - left + 1, max_len)
                # print(f"left: {left}, max: {max_len}: char: {char}")

        return max_len


def test():
    func = Solution().lengthOfLongestSubstring
    cases = """abcabcbb
bbbbbb
pwwkew
abcdefghijklmn9999999999999999999999
bb
ab
a
nfpdmpi
tmmzuxt
aabaab!bb"""
    for item in cases.split("\n"):
        print(item, "==>", func(item))


if __name__ == '__main__':
    test()
