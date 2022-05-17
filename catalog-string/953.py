# 953. 验证外星语词典
# https://leetcode.cn/problems/verifying-an-alien-dictionary/


# 我的解法
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}

        def isRightCharOrder(a, b):
            return order_map[a] < order_map[b]

        def isRightWordOrder(x, y):
            length = min(len(x), len(y))
            same_len = 0
            for i in range(length):
                if x[i] == y[i]:
                    same_len += 1
                    continue

                if not isRightCharOrder(x[i], y[i]):
                    return False
                else:
                    return True

            if same_len == length and len(y) == same_len and len(x) != length:
                return False

            return True

        for i in range(len(words) - 1):
            if not isRightWordOrder(words[i], words[i + 1]):
                return False

        return True
