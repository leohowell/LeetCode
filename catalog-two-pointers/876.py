# 876. 链表的中间结点
# https://leetcode-cn.com/problems/middle-of-the-linked-list/

# 我的解法 (同官方解法，快慢指针法)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        left, right = head, head
        flag = True
        while right is not None:
            right = right.next
            flag = not flag
            if flag:
                left = left.next
        return left
