# -*- coding: utf-8 -*-

from tools.binary_tree import TreeNode, get_linked_list


def level_order(root, level, res):
    if not root:
        return
    if len(res) < level + 1:
        res.append([])
    res[level].append(root.val)
    level_order(root.left, level+1, res)
    level_order(root.right, level+1, res)
    return res


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = level_order(root, 0, [])
        for index in range(1, len(res), 2):
            res[index] = res[index][::-1]
        return res

head = get_linked_list('[3,9,20,null,null,15,7]')
print(Solution().zigzagLevelOrder(head))

