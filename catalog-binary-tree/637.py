from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 先搞清楚如何BFS遍历

        output = []

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for i in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg = sum(level_nodes) / len(level_nodes)
            output.append(avg)
        return output


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

res = Solution().averageOfLevels(root)
print(res)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

res = Solution().averageOfLevels(root)
print(res)
