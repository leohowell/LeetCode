# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        node = head
        while head.val == val:
            head = head.next
            node = head
            if not head:
                return head

        while node.next:
            if node.next.val == val:
                if not node.next.next:
                    node.next = None
                    return head
                elif node.next.next.val == val:
                    cand = node.next.next.next
                    while cand:
                        if cand.val == val:
                            cand = cand.next
                        else:
                            break
                    if not cand:
                        node.next = None
                        return head
                    else:
                        node.next = cand
                else:
                    node.next = node.next.next
            node = node.next
        return head
