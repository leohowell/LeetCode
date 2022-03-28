# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_deep = self.maxDepth(root.left)
        right_deep = self.maxDepth(root.right)
        return left_deep+1 if left_deep > right_deep else right_deep+1
