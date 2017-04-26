# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            root = TreeNode(postorder.pop())
            inorder_index = inorder.index(root.val)
            root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
            root.left = self.buildTree(inorder[:inorder_index], postorder)
            return root


def pre_order(tree):
    if not tree:
        return
    print tree.val, '->',
    pre_order(tree.left)
    pre_order(tree.right)


s = Solution()
tree = s.buildTree(['d', 'b', 'e', 'a', 'c'], ['d', 'e', 'b', 'c', 'a'])
pre_order(tree)
