# 394. 字符串解码
# https://leetcode.cn/problems/decode-string/

# 我的解法
class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        n = len(s)

        stack = []

        num = 0
        for i in range(n):
            # print(num, stack, ans)
            char = s[i]

            if char.isdigit():
                if num:
                    num = num * 10 + int(char)
                else:
                    num = int(char)
                continue

            if char == "[":
                stack.append(num)
                stack.append(char)
                num = 0
                continue

            if char == "]":
                pop_chars = []
                pop_num = 0
                while stack:
                    pop_char = stack.pop()
                    if pop_char == '[':
                        pop_num = stack.pop()
                        break
                    else:
                        pop_chars.append(pop_char)
                decode_chars = ''.join(pop_chars[::-1]) * pop_num
                if stack:
                    stack.append(decode_chars)
                else:
                    ans.append(decode_chars)
                num = 0
                continue

            if stack:
                stack.append(char)
            else:
                ans.append(char)
            num = 0

        return "".join(ans)
