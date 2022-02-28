from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"""<Node val={self.val} left={self.left} right={self.right}>"""


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
        current_level = array[pointer: pointer + offset]
        pointer += offset
        new_last_nodes = []
        for index, node in enumerate(last_nodes):
            left_index = index * 2
            if left_index >= len(current_level):
                break
            left = current_level[index * 2]
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


null = None


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        _, val = self.dfs(root, target)
        return val

    def dfs(self, root, target):
        if not root:
            return None, None

        gap = root.val - target
        root_gap = abs(gap)

        if root_gap < 0.5:
            return root_gap, root.val

        if gap > 0:
            sub_gap, val = self.dfs(root.left, target)
        else:
            sub_gap, val = self.dfs(root.right, target)

        if sub_gap is None or root_gap < sub_gap:
            return root_gap, root.val
        else:
            return sub_gap, val


def test():
    func = Solution().closestValue
    root1 = create_binary_tree_from_level_order_list([28,12,45,4,24,35,47,2,9,14,25,31,42,46,48,0,3,8,11,13,20,null,26,30,33,41,43,null,null,null,49,null,1,null,null,7,null,10,null,null,null,17,22,null,27,29,null,32,34,36,null,null,44,null,null,null,null,6,null,null,null,16,18,21,23,null,null,null,null,null,null,null,null,null,37,null,null,5,null,15,null,null,19,null,null,null,null,null,40,null,null,null,null,null,null,39,null,38])
    print(func(root1, 2.000000))
    root8 = create_binary_tree_from_level_order_list([4,2,5,1,3])
    print(func(root8, 3.7))


if __name__ == '__main__':
    test()
