# -*- coding: utf-8 -*-

# Definition for singly-linked list.

import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        if not head.next:
            return head

        new_head = head
        node = head.next
        cache_next = head.next
        head.next = None
        while cache_next:
            cache_next = node.next
            node.next = new_head
            new_head = node
            node = cache_next

        return new_head

a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')

a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
head = s.reverseList(a)

node = head
while node:
    print node.val, node.next
    node = node.next
    time.sleep(0.5)
