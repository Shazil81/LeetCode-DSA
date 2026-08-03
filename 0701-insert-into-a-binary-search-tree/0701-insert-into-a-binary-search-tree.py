# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Condition
        if root is None:
            return TreeNode(val)
        curr = root
        # Loop chalao Infinite lekin break kr dena hai
        while True:
            if val < curr.val:
                # kyun ki add kuchh bhi kr lo last me hi ja k hoga kyun ki tree bna hua h
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break  # jha pe add hua wha pe break kr do kahani khtm
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        return root