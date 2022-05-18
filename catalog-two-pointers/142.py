# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        if head == head.next:
            return head

        # 快慢指针
        fast, slow, start = head, head, head

        while True:
            fast = fast.next
            if not fast:
                return None

            fast = fast.next
            if not fast:
                return None

            slow = slow.next
            if fast == slow:
                break

        while True:
            if slow == start:
                return slow
            slow = slow.next
            start = start.next
