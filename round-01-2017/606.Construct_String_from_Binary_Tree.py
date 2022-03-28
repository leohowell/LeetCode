# -*- coding: utf-8 -*-

from tools.binary_tree import get_linked_list


def pre_order(root):
    if not root:
        return ''
    if not root.right and not root.left:
        return str(root.val)
    left = pre_order(root.left)
    right = pre_order(root.right)
    if left == '' and right != '':
        left = '()'
    if not left.startswith('('):
        left = '({})'.format(left)
    if not right.startswith('(') and right != '':
        right = '({})'.format(right)
    return '{}{}{}'.format(root.val, left, right)


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return pre_order(t)


head = get_linked_list('[1,2,3,4]')
print(pre_order(head))
head2 = get_linked_list('[1,2,3,null,4]')
print(pre_order(head2))
head3 = get_linked_list('[]')
print(pre_order(head3))
