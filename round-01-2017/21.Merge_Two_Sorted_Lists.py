# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            head = l1
            node = l1
            l1 = l1.next
        else:
            head = l2
            node = l2
            l2 = l2.next

        while l2:
            if not l1:
                break
            if l1.val < l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return head
