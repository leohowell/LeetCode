# -*- coding: utf-8 -*-

"""
Given an integer, write an algorithm to convert it to hexadecimal.
For negative integer, two’s complement method is used.

Note:

1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s.
   If the number is zero, it is represented by a single zero character '0';
   otherwise, the first character in the hexadecimal string will not be
   the zero character.
3. The given number is guaranteed to fit within the range of a 32-bit
   signed integer.
4. You must not use any method provided by the library which converts/formats
   the number to hex directly.

Example 1:

Input:
26

Output:
"1a"

Example 2:

Input:
-1

Output:
"ffffffff"
"""


class Solution(object):
    HEX_TABLE = {
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
    }
    MASK = 0xffffffff

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        if num < 0:
            num = (-num ^ self.MASK) + 1
        tmp = []
        while num:
            quo = num % 16
            quo = self.HEX_TABLE.get(quo, str(quo))
            num /= 16
            tmp.append(quo)
        return ''.join(tmp[::-1])
