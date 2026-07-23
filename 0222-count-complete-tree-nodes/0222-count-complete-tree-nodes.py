# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TC : log(n) hai
    # step 1 count kro left nodes ko
    def countLeft(self, root):
        count = 0
        while root:
            count+=1
            root = root.left
        return count
    # step 2 count kro right nodes ko
    def countRight(self, root):
        count = 0
        while root:
            count+=1
            root = root.right
        return count
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        leftHeight = self.countLeft(root)
        rightHeight = self.countRight(root)
        # left height baarabr rhega tb ye formula work krega
        if leftHeight == rightHeight:
            return (2 ** leftHeight) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)