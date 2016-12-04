# -*- coding: utf-8 -*-

"""
Given two non-negative numbers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

1. The length of both num1 and num2 is < 5100.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert
   the inputs to integer directly.
"""


class Solution(object):
    STRING_ADD_TABLE = {
        ('0', '0'): ('0', '0'),
        ('0', '1'): ('0', '1'),
        ('0', '2'): ('0', '2'),
        ('0', '3'): ('0', '3'),
        ('0', '4'): ('0', '4'),
        ('0', '5'): ('0', '5'),
        ('0', '6'): ('0', '6'),
        ('0', '7'): ('0', '7'),
        ('0', '8'): ('0', '8'),
        ('0', '9'): ('0', '9'),

        ('1', '1'): ('0', '2'),
        ('1', '2'): ('0', '3'),
        ('1', '3'): ('0', '4'),
        ('1', '4'): ('0', '5'),
        ('1', '5'): ('0', '6'),
        ('1', '6'): ('0', '7'),
        ('1', '7'): ('0', '8'),
        ('1', '8'): ('0', '9'),
        ('1', '9'): ('1', '0'),

        ('2', '2'): ('0', '4'),
        ('2', '3'): ('0', '5'),
        ('2', '4'): ('0', '6'),
        ('2', '5'): ('0', '7'),
        ('2', '6'): ('0', '8'),
        ('2', '7'): ('0', '9'),
        ('2', '8'): ('1', '0'),
        ('2', '9'): ('1', '1'),

        ('3', '3'): ('0', '6'),
        ('3', '4'): ('0', '7'),
        ('3', '5'): ('0', '8'),
        ('3', '6'): ('0', '9'),
        ('3', '7'): ('1', '0'),
        ('3', '8'): ('1', '1'),
        ('3', '9'): ('1', '2'),

        ('4', '4'): ('0', '8'),
        ('4', '5'): ('0', '9'),
        ('4', '6'): ('1', '0'),
        ('4', '7'): ('1', '1'),
        ('4', '8'): ('1', '2'),
        ('4', '9'): ('1', '3'),

        ('5', '5'): ('1', '0'),
        ('5', '6'): ('1', '1'),
        ('5', '7'): ('1', '2'),
        ('5', '8'): ('1', '3'),
        ('5', '9'): ('1', '4'),

        ('6', '6'): ('1', '2'),
        ('6', '7'): ('1', '3'),
        ('6', '8'): ('1', '4'),
        ('6', '9'): ('1', '5'),

        ('7', '7'): ('1', '4'),
        ('7', '8'): ('1', '5'),
        ('7', '9'): ('1', '6'),

        ('8', '8'): ('1', '6'),
        ('8', '9'): ('1', '7'),

        ('9', '9'): ('1', '8'),
    }

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num1_len = list(num1[::-1]), len(num1)
        num2, num2_len = list(num2[::-1]), len(num2)

        diff = num1_len - num2_len
        if diff > 0:
            high = num1[num2_len:]
            num1 = num1[:num2_len]
        elif diff < 0:
            high = num2[num1_len:]
            num2 = num2[:num1_len]
        else:
            high = []

        sum = []
        store_carry = "0"
        for i, char in enumerate(num1):
            carry, tail = self.string_add(char, num2[i])
            if store_carry == "1":
                extra_carry, tail = self.string_add(store_carry, tail)
                if "1" in (carry, extra_carry):
                    store_carry = "1"
                else:
                    store_carry = "0"
            else:
                store_carry = carry
            sum.append(tail)

        for i, char in enumerate(high):
            store_carry, tail = self.string_add(char, store_carry)
            high[i] = tail

        if store_carry == "1":
            high.append(store_carry)

        return ''.join((sum + high)[::-1])

    def string_add(self, a, b):
        return self.STRING_ADD_TABLE.get((a, b)) or \
               self.STRING_ADD_TABLE.get((b, a))
