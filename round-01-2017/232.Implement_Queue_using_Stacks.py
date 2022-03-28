# -*- coding: utf-8 -*-


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__values = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.__values.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.__values:
            top = self.__values[0]
            del self.__values[0]
            return top

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.__values:
            return self.__values[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return bool(not self.__values)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
