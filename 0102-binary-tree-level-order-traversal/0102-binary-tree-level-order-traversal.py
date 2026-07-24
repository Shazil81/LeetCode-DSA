# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order traversal (BFS - Breadth First Search)
        res = []
        queue = deque([])

        if root is None: # base case
            return []

        queue.append(root)

        while len(queue) != 0:
            curr_level = []

            for _ in range(len(queue)):
                e = queue.popleft()
                curr_level.append(e.val)
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
            res.append(curr_level)
        
        return res