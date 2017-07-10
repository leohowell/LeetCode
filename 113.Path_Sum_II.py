# -*- coding: utf-8 -*-

from tools.binary_tree import get_linked_list


def per_order(root, target, inherit):
    if not root:
        return []
    if not root.left and not root.right:
        if sum(inherit) + root.val == target:
            inherit.append(root.val)
            return [inherit]
        else:
            return []
    new_inherit = []
    new_inherit.extend(inherit)
    new_inherit.append(root.val)
    right_inherit = [x for x in new_inherit]
    left = per_order(root.left, target, new_inherit)
    right = per_order(root.right, target, right_inherit)
    result = []
    for item in left:
        result.append(item)
    for item in right:
        result.append(item)
    return result


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return per_order(root, sum, [])


head = get_linked_list('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
print(per_order(head, 22, []))
print(per_order(None, 0, []))
head2 = get_linked_list('[0, 1, 1]')
print(per_order(head2, 1, []))

