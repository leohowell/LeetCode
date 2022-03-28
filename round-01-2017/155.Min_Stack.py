# -*- coding: utf-8 -*-


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.order = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.values.append(x)
        p = self.search_insert(x)
        self.order.insert(p, x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.values:
            return None
        x = self.values.pop()
        self.order.remove(x)

    def top(self):
        """
        :rtype: int
        """
        if not self.values:
            return None
        return self.values[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.order:
            return None
        return self.order[0]

    def search_insert(self, x):
        low = 0
        high = len(self.order)
        while low < high:
            mid = (low + high) / 2
            if x < self.order[mid]:
                high = mid
            elif x == self.order[mid]:
                return mid
            else:
                low = mid + 1
        return low


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print obj.getMin()
obj.pop()
print obj.top()
print obj.getMin()
