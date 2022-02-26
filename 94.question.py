# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"""<Node val={self.val} left={self.left} right={self.right}>"""


null = None


def list_to_pre_order_binary_tree(root):
    """基于前序遍历列表生成二叉树"""

    root_node = None
    last_node = None
    leaf = None
    for val in root:
        if val is null:
            if not last_node:
                return None
            else:
                if leaf == "left":
                    leaf = "right"
                else:
                    print("Error")
        else:
            node = TreeNode(val=val)
            if not last_node:
                root_node = node
                last_node = node
                leaf = "left"
            else:
                setattr(last_node, leaf, node)
                last_node = node
                leaf = "left"
    return root_node


def create_binary_tree_from_pre_order_list(array):
    """从先序列表中生成二叉树"""
    if not array:
        return null, array

    val = array[0]
    # 如果val是null
    if val is null:
        return null, array[1:]

    node = TreeNode(val=val)
    if len(array) == 1:
        return node, array[1:]

    node.left, left = create_binary_tree_from_pre_order_list(array[1:])
    node.right, left = create_binary_tree_from_pre_order_list(left)
    return node, left


def create_binary_tree_from_level_order_list(array):
    """
    从层次排序列表中生成二叉树
    文档: https://support.leetcode-cn.com/hc/kb/article/1194353/
    """
    if not array:
        return None

    root = TreeNode(val=array[0])
    last_nodes = [root]

    pointer = 1
    while pointer < len(array):
        offset = len(last_nodes) * 2
        # 当前值
        current_level = array[pointer: pointer+offset]
        pointer += offset
        new_last_nodes = []
        for index, node in enumerate(last_nodes):
            left_index = index*2
            if left_index >= len(current_level):
                break
            left = current_level[index*2]
            if left:
                left = TreeNode(val=left)
                new_last_nodes.append(left)
                node.left = left

            right_index = index * 2 + 1
            if right_index >= len(current_level):
                break
            right = current_level[right_index]
            if right:
                right = TreeNode(val=right)
                new_last_nodes.append(right)
                node.right = right
        last_nodes = new_last_nodes

    return root


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.middle_traversal(root)

    @classmethod
    def middle_traversal(cls, node):
        output = []
        if node.left:
            output = cls.middle_traversal(node.left)
        if node:
            output.append(node.val)
        if node.right:
            output += cls.middle_traversal(node.right)
        return output


def test():
    func = Solution().inorderTraversal
    root1 = create_binary_tree_from_level_order_list([1, null, 2, 3])
    root2 = create_binary_tree_from_level_order_list([1, 2, null, 3])
    print(func(root1))
    print(func(root2))


if __name__ == '__main__':
    test()
