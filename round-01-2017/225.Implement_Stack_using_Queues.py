# -*- coding: utf-8 -*-


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.values.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.values:
            return None
        self.values.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.values:
            return None
        return self.values[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.values == []


b = Stack()
print b.empty()
