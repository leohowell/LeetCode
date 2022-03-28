# -*- coding: utf-8 -*-


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        comp = 0
        loop = 0
        while num != 0:
            comp += (~(num % 2) + 2) * (2 ** loop)
            num >>= 1
            loop += 1
        return comp


def dec2bin(n):
    b = []
    while n != 0:
        b.append(n % 2)
        n >>= 1
    return b


def bin2dec(arrays):
    total = 0
    for i, item in enumerate(arrays):
        total += item * (2 ** i)
    return total


arrays = dec2bin(34)
print bin2dec(arrays)
print bin(34)

b = Solution()
print b.findComplement(10086)
