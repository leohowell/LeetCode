# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.pre_order(root, 0, res)
        for level in res[1:]:
            l = len(level)
            if l % 2 != 0:
                return False
            if level[:l//2] != level[l//2:][::-1]:
                return False
        return True

    @classmethod
    def pre_order(cls, root, level, res):
        if len(res) < level + 1:
            res.append([])
        if not root:
            res[level].append(None)
            return
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

print(Solution().isSymmetric(nodes['a']))

