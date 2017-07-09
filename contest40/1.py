# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

res = []


def pre_order(tree, level, res):
    if not tree:
        return
    if len(res) < level + 1:
        res.append([])
    res[level].append(tree.val)
    pre_order(tree.left, level + 1, res)
    pre_order(tree.right, level + 1, res)
    return res


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        self.pre_order(root, 0, res)
        return [sum(x) / len(x) for x in res]

    @staticmethod
    def pre_order(tree, level, res):
        if not tree:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(tree.val)
        pre_order(tree.left, level + 1, res)
        pre_order(tree.right, level + 1, res)
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


print(Solution().averageOfLevels(nodes['a']))
pre_order(nodes['a'], 0, res)
print(res)
