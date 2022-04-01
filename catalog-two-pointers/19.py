# 19. 删除链表的倒数第 N 个结点
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

# 我的解法 快慢指针(基本同官方题解)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        b = ListNode(val="x", next=head)
        a = ListNode(val="x",next=b)

        left, right = a, a
        cnt = n
        while right.next:
            right = right.next
            if cnt > 0:
                cnt -= 1
            elif cnt == 0:
                left = left.next
        left.next = left.next.next

        while a and a.val == "x":
            a = a.next

        return a
