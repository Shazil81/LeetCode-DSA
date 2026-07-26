# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BfS ka use kr k solve ho rha h
        if root is None:
            return []
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                e = queue.popleft()
                # level size k last me aayega jo node wohi to hoga right view me
                if i == level_size - 1:
                    res.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return res            