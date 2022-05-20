# 83. 删除排序链表中的重复元素
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        point = head
        while True:
            if not point or not point.next:
                break

            if point.val == point.next.val:
                point.next = point.next.next
            else:
                point = point.next

        return head
