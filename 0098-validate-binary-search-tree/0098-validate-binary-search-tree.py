# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Using range
        limit = [float("-inf"), float("inf")]
        def solve(node, limit):
            if not node:
                return True
            if not limit[0] < node.val < limit[1]:
                return False
            left = solve(node.left, [limit[0], node.val])
            if left == False:
                return False
            right = solve(node.right, [node.val, limit[1]])
            return left and right
        return solve(root, limit)