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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        output += self.postorderTraversal(root.left)
        output += self.postorderTraversal(root.right)
        output.append(root.val)
        return output


def test():
    func = Solution().postorderTraversal
    root1 = create_binary_tree_from_level_order_list([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1])
    print(func(root1))
    root2 = create_binary_tree_from_level_order_list([1,null,2,3])
    print(func(root2))
    root3 = create_binary_tree_from_level_order_list([])
    print(func(root3))
    root4 = create_binary_tree_from_level_order_list([1])
    print(func(root4))
    root5 = create_binary_tree_from_level_order_list([1, 2])
    print(func(root5))
    root6 = create_binary_tree_from_level_order_list([1,null,2])
    print(func(root6))



if __name__ == '__main__':
    test()
