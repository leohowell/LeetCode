# 141. 环形链表
# https://leetcode.cn/problems/linked-list-cycle/

# Floyd判圈算法
# Floyd判圈算法(Floyd Cycle Detection Algorithm)，又称龟兔赛跑算法(Tortoise and Hare Algorithm)
# 如果有限状态机、迭代函数或者链表上存在环，那么在某个环上以不同速度前进的2个指针必定会在某个时刻相遇。
# 同时显然地，如果从同一个起点(即使这个起点不在某个环上)同时开始以不同速度前进的2个指针最终相遇，
# 那么可以判定存在一个环，且可以求出2者相遇处所在的环的起点与长度。

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 查看了题解思路后的解法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        # 快指针一次移动两步，慢指针一次移动一步
        # 快指针一定会进入无限循环，并且与慢指针相遇

        if not head:
            return False

        if head.next is None:
            return False

        slow, fast = head, head.next

        if fast == slow:
            return True

        while True:
            if not fast:
                return False

            fast = fast.next
            if not fast:
                return False

            fast = fast.next
            if not fast:
                return False

            slow = slow.next
            if fast == slow:
                return True

# 哈希表解法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        his = {id(head), }
        while True:
            head = head.next
            if not head:
                return False

            if id(head) in his:
                return True
            else:
                his.add(id(head))


# [3,2,0,-4]
# 1
# [1,1,1,1,1]
# 0
# [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# 9
# [1,2]
# 0
# [1]
# -1
# [1]
# 0
# []
# -1
# [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
# -1
