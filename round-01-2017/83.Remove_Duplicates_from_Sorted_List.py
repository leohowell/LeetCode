# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head

        if not head:
            return head

        while head and head.next:
            while head.val == head.next.val:
                head.next = head.next.next
                if not head.next:
                    break
            head = head.next

        return start

