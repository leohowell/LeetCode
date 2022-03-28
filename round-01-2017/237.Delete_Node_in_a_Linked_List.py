# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next


a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
b.next = a
c.next = b
d.next = c

s = Solution()
s.deleteNode(d)
node = d
while node:
    print node.val, node.next
    node = node.next
