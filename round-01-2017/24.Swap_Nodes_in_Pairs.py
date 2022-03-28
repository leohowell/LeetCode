# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        node1 = head
        if node1.next:
            head = node1.next

        while node1:
            node2 = node1.next
            if node2:
                node3 = node2.next
            else:
                break

            if node3 and node3.next:
                node1.next = node3.next
            else:
                node1.next = node3
            node2.next = node1
            node1 = node3
        return head
