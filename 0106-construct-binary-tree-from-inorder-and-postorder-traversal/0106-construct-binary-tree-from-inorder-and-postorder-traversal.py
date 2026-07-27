# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
         # step 1
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        preorder = collections.deque(postorder)
        
        def solve(start, end):
            if start > end:
                return None
            # root bana
            root = TreeNode(postorder.pop())
            # mid yaani inorder me root ka index
            mid = mapping[root.val]
            # right subtree create
            root.right = solve(mid+1, end)
            # Left subtree create
            root.left = solve(start, mid-1)
            
            return root
        
        return solve(0, len(postorder)-1)