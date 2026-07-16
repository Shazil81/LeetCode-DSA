# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def solve(root):
            if root is None:
                return 0
            leftheight = solve(root.left)
            rightheight = solve(root.right)
            # ba yhi condition se max path mil jayega
            self.diameter = max(self.diameter, leftheight + rightheight)
            return 1 + max(leftheight, rightheight)
        solve(root)
        return self.diameter