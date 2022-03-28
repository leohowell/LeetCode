# -*- coding: utf-8 -*-


def foo(A):
    """
    gap: current two consecutive number's difference
    conti: extra nums length except 3 elements
    """
    if len(A) < 3:
        return 0
    conti = 0
    gap = A[1] - A[0]
    last = A[1]
    result = 0
    for n in A[2:]:
        if n - last == gap:
            conti += 1
            result += conti
            last = n
        else:
            conti = 0
            gap = n - last
            last = n
    return result


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return foo(A)

print(foo([1, 2, 3, 4, 6, 8, 9, 10, 11]))
