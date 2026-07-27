# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # step 1
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        preorder = collections.deque(preorder)
        
        def solve(start, end):
            if start > end:
                return None
            # root bana
            root = TreeNode(preorder.popleft())
            # mid yaani inorder me root ka index
            mid = mapping[root.val]
            # Left subtree create
            root.left = solve(start, mid-1)
            # right subtree create
            root.right = solve(mid+1, end)

            return root
        
        return solve(0, len(preorder)-1)



            
