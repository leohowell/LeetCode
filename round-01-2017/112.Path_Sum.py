# -*- coding: utf-8 -*-

from tools.binary_tree import get_linked_list


def pre_order(root, target, inherit):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val + inherit == target
    left = pre_order(root.left, target, inherit + root.val)
    right = pre_order(root.right, target, inherit + root.val)
    return left or right

def path_sum(root, target):
    if not root:
        return False
    return pre_order(root, target, 0)


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return pre_order(root, sum, target)

head = get_linked_list('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
print(path_sum(head, 22))
head2 = get_linked_list('[]')
print(path_sum(head2, 9))

