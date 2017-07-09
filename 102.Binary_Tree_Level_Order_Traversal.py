# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        return self.pre_order(root, 0, res)

    @classmethod
    def pre_order(cls, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        cls.pre_order(root.left, level+1, res)
        cls.pre_order(root.right, level+1, res)
        return res


nodes = {}
for char in 'abcdefghijklmnopqrstuvwxyz':
    nodes[char] = TreeNode(ord(char))

nodes['a'].left = nodes['b']
nodes['a'].right = nodes['c']
nodes['b'].left = nodes['d']
nodes['b'].right = nodes['e']
nodes['c'].left = nodes['f']
nodes['c'].right = nodes['g']
nodes['d'].left = nodes['h']
nodes['d'].right = nodes['i']
nodes['e'].left = nodes['j']
nodes['e'].right = nodes['k']
nodes['f'].left = nodes['l']
nodes['f'].right = nodes['m']
nodes['g'].left = nodes['n']
nodes['g'].right = nodes['o']

print(Solution().levelOrder(nodes['a']))

