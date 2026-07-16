# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion se krte hain ye zyada optimal hai
        def solve(root):
            if root is None:
                return 0
            leftheight = solve(root.left)
            rightheight = solve(root.right)
            return 1 + max(leftheight, rightheight)
        return solve(root)
