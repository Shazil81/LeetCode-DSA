# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        # bs height pattern pe question hai
        def solve(root):
            if root is None:
                return 0
            LH = solve(root.left)
            if LH < 0:
                LH = 0
            RH = solve(root.right)
            if RH < 0:
                RH = 0
            self.maxi = max(self.maxi, LH + root.val + RH)
            return root.val + max(LH, RH)
        solve(root)
        return self.maxi