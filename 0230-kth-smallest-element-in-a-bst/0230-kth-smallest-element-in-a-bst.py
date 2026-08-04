# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Ek ye solution optimized isme TC:O(n) SC:O(1)  Most optimal
        # Morris algorithm // Inorder Traversal // BST Inorder always sorted
        count = 0
        ans = None
        curr = root
        while curr is not None:
            if curr.left is None:
                count += 1
                if count == k:
                    ans = curr.val
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right is not None and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    count += 1
                    if count == k:
                        ans = curr.val
                    curr = curr.right
        return ans
        