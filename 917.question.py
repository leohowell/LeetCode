# 仅仅翻转字母

import string


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [char for char in s if self.is_letter(char)]
        new_orders = []
        for char in s:
            if self.is_letter(char):
                new_orders.append(stack.pop())
            else:
                new_orders.append(char)

        return "".join(new_orders)

    @classmethod
    def is_letter(cls, char: str) -> bool:
        return char[0] in string.ascii_letters


def test():
    cases = {
        "ab-cd": "dc-ba",
        "a-bC-dEf-ghIj": "j-Ih-gfE-dCba",
        "Test1ng-Leet=code-Q!": "Qedo1ct-eeLg=ntse-T!",
        "": "",
        "ab": "ba",
        "---": "---",
    }
    func = Solution().reverseOnlyLetters
    for k, v in cases.items():
        assert func(k) == v


if __name__ == '__main__':
    test()
