# 821. 字符的最短距离
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/

# 我的解法
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # 尝试使用双指针处理
        answer = []
        left, right = -len(s), -len(s)
        for i in range(len(s)):
            if s[i] == c:
                left = right
                right = i

                if left == -len(s):  # 当遇到第一个c
                    for j in range(right, -1, -1):
                        answer.append(j)
                else:  # 当在两个c中间时
                    mid = int((right - left) / 2 + left) + 1
                    if mid == left:
                        answer.append(0)
                        continue

                    # e1111111e
                    for j in range(left + 1, mid):
                        answer.append(j - left)

                    for j in range(mid, right + 1):
                        answer.append(right - j)

            elif i == len(s) - 1:  # 当循环到最后一个字符不是c
                for j in range(right + 1, len(s)):
                    answer.append(j - right)

        return answer


# 官方题解 左右两次遍历
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []

        index = -len(s)
        for i in range(len(s)):
            if s[i] == c:
                index = i
                ans.append(0)
            else:
                ans.append(i - index)

        index = 2 * len(s)
        for i in range(len(s))[::-1]:
            if s[i] == c:
                index = i
            else:
                ans[i] = min(index - i, ans[i])
        return ans
