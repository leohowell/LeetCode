# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add(self, node, value):
        node.val = node.val + value
        if node.val > 9:
            node.val = node.val - 10
            if node.next:
                return self.add(node.next, 1)
            else:
                node.next = ListNode(1)
                node.next.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = l1

        if not l1:
            return l2
        if not l2:
            return l1

        while True:
            self.add(l1, l2.val)

            if l1.next:
                l1 = l1.next
            else:
                l1.next = l2.next
                break

            if l2.next:
                l2 = l2.next
            else:
                break
        return out
