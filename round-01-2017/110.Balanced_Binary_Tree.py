# -*- coding: utf-8 -*-

from tools.binary_tree import get_linked_list, show_graph


def tree_height(root):
    if not root:
        return 0
    return max(tree_height(root.left), tree_height(root.right)) + 1


def is_balanced_binary_tree(root):
    if not root:
        return True

    if abs(tree_height(root.left) - tree_height(root.right)) <= 1:
        return is_balanced_binary_tree(root.left) and \
               is_balanced_binary_tree(root.right)
    else:
        return False


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return is_balanced_binary_tree(root)

head = get_linked_list('[1,null,2,null,3]')
print(tree_height(head))
print(tree_height(head.right))
show_graph(head)
print(is_balanced_binary_tree(head))

