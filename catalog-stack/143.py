# 143. 重排链表
# https://leetcode.cn/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 我的解答
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        stack = []

        right = head
        while right:
            stack.append(right)
            right = right.next

        # 1 2 3 4 = 1 4 2 3
        # 1 2 3 4 5 = 1 5 2 4 3

        right = head

        for i in range(len(stack)):
            if i % 2 == 0:
                val = stack.pop()
                val.next = right.next
                right.next = val
                right = val
            else:
                right = right.next
        right.next = None
