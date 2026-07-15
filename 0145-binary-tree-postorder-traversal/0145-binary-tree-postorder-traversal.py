# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Postorder means [Left - Right - Root]
        res = []
        # Recursion se krte hain
        def postorder(node):
            if node == None:
                return
            
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        
        postorder(root)
        return res