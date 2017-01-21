# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        tag = '__tag__'
        head.val = tag
        while head and head.next:
            if head.next.val == tag:
                return True
            head.next.val = tag
            head = head.next
        return False


a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')


a.next = b
b.next = c
c.next = d
d.next = a

s = Solution()
print s.hasCycle(a)

print a.val
print b.val
print c.val
print d.val
