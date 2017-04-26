# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder.pop(0))
            inorder_index = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:inorder_index])
            root.right = self.buildTree(preorder, inorder[inorder_index+1:])
            return root


def post_order(tree):
    if not tree:
        return None
    post_order(tree.left)
    post_order(tree.right)
    print tree.val, '->',


s = Solution()
tree = s.buildTree(['a', 'b', 'd', 'e', 'c'], ['d', 'b', 'e', 'a', 'c'])
post_order(tree)
