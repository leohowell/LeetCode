# 206. 反转链表
# https://leetcode.cn/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # a b c
        # t = b.next
        # b.next = a

        if not head:
            return head

        if not head.next:
            return head

        ans = head
        head = head.next
        ans.next = None

        while True:
            t = head.next
            head.next = ans
            ans = head
            if not t:
                return ans
            head = t
