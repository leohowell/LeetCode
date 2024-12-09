# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序遍历 左-中-右
        # 左子树所有节点小于当前节点
        # 右子树所有节点大于当前节点

        # 236
        # 104, 701
        # None, 227, None, 911

        last_val = None
        min_val = 10**5 + 1
        for val in self.binary_search_tree_in_order(root):
            if last_val is not None:
                min_val = min(min_val, val - last_val)
            last_val = val

        return min_val

    def binary_search_tree_in_order(self, root: Optional[TreeNode]):
        if root:
            yield from self.binary_search_tree_in_order(root.left)
            yield root.val
            yield from self.binary_search_tree_in_order(root.right)


def array_to_tree(array):
    if not array:  # 如果数组为空，返回空树
        return None

    # 创建根节点
    root = TreeNode(array[0])
    queue = deque([root])  # 队列用于按层次构建二叉树
    index = 1  # 当前数组索引

    while queue and index < len(array):
        node = queue.popleft()  # 从队列中取出当前节点

        # 构建左子节点
        if index < len(array) and array[index] is not None:
            node.left = TreeNode(array[index])
            queue.append(node.left)
        index += 1

        # 构建右子节点
        if index < len(array) and array[index] is not None:
            node.right = TreeNode(array[index])
            queue.append(node.right)
        index += 1

    return root


if __name__ == "__main__":
    values = [4, 2, 6, 1, 3]
    root = array_to_tree(values)
    res = Solution().getMinimumDifference(root)
    print(res)

    values = [236, 104, 701, None, 227, None, 911]
    root = array_to_tree(values)
    res = Solution().getMinimumDifference(root)
    print(res)
