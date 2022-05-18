# 202. 快乐数
# https://leetcode.cn/problems/happy-number/


# 快慢指针, 看了题解思路
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(val):
            res = 0
            while True:
                if val < 10:
                    return res + val * val
                else:
                    num = val % 10
                    res += num * num
                    val = val // 10

        fast, slow = getNext(n), n

        if fast == 1:
            return True

        if fast == slow:
            return False

        while True:
            fast = getNext(fast)
            if fast == 1:
                return True

            fast = getNext(fast)
            if fast == 1:
                return True

            slow = getNext(slow)
            if fast == slow:
                return False


# 哈希表法
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while True:
            value = sum(int(x)**2 for x in str(n))
            if value == 1:
                return True
            elif value in cache:
                return False
            else:
                cache.add(n)
                n = value


# 19
# 2
# 100
# 82
# 68
# 1
# 19999
# 151123
