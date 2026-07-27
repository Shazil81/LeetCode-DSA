# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, res):
        if root is None:
            return
        res.append(root)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Ye code optimal hai (Morris Algorithm)
        curr = root
        while curr:
            if curr.left:
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                rightmost.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
        
        
        



        