from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 分治
        # divide-conquer-combine

        length = len(nums)

        # conquer
        if length == 1:
            return TreeNode(nums[0])
        elif length == 2:
            root = TreeNode(nums[1])
            left = TreeNode(nums[0])
            root.left = left
            return root
        elif length == 3:
            root = TreeNode(nums[1])
            left = TreeNode(nums[0])
            right = TreeNode(nums[2])
            root.left = left
            root.right = right
            return root

        # divide
        divide = length // 2

        root = TreeNode(nums[divide])
        left_nums = nums[:divide]
        right_nums = nums[divide + 1 :]

        # combine
        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)

        return root

    def sortedArrayToBST001(self, nums: List[int]) -> Optional[TreeNode]:
        # 单链形 二叉树
        # 有序列表转换为二叉搜索树

        # 1 2 3 4 5 6
        # 1 2 3 4 5 6 7

        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])

        divide = length // 2

        root = TreeNode(nums[divide])

        last_left = root
        for val in nums[:divide][::-1]:
            node = TreeNode(val)
            last_left.left = node
            last_left = node

        last_right = root
        for val in nums[divide + 1 :]:
            node = TreeNode(val)
            last_right.right = node
            last_right = node

        return root
