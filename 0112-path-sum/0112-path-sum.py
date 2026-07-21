# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target, path_sum):
            if not node:
                return False
            path_sum += node.val
            # leaf node tk hoga tb hi return krna h true
            if node.left is None and node.right is None:
                if path_sum == target:
                    return True
            left = dfs(node.left, target, path_sum)
            right = dfs(node.right, target, path_sum)
            if left == True or right == True:
                return True
            return False

        return dfs(root, targetSum, 0)