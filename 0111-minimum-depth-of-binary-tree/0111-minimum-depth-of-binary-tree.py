# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # bfs zyada optimal hai kyun ki early stopping hoga
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, depth = queue.popleft()
            # main logic yhi hai ki jha pe mila leaf node pehle wohi wala depth hoga min
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
