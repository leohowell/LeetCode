# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.deep(root)

    def deep(self, root, ex=0):
        if root:
            ex += 1
        else:
            return ex

        if not root.left and not root.right:
            return ex

        depth_left = self.deep(root.left, ex)
        depth_right = self.deep(root.right, ex)

        if depth_left == ex:
            return depth_right
        elif depth_right == ex:
            return depth_left

        if depth_left > depth_right:
            return depth_right
        else:
            return depth_left


a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')
g = TreeNode('g')
h = TreeNode('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h

s = Solution()
print s.minDepth(a)

