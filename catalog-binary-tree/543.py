# 543. 二叉树的直径
# https://leetcode.cn/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, _, val = self.foo(root)
        return val

    def foo(self, root):
        left, right, left_max, right_max = 0, 0, 0, 0
        if not root:
            return left, right, 0
        if root.left:
            a, b, left_max = self.foo(root.left)
            left = max(a, b) + 1
        if root.right:
            a, b, right_max  = self.foo(root.right)
            right = max(a, b) + 1
        return left, right, max(left_max, right_max, left + right)
