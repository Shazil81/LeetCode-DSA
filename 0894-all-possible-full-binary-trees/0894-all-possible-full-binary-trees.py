# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Base case
        if n == 1:
            return [TreeNode(0)]
        
        # Even Nodes me Full Bianry Tree impossible hai
        if n%2 == 0:
            return []
        
        res = []

        for i in range(1, n, 2): # 2 steps chal rha h
            left_count = i
            right_count = n - 1 - i

            left_trees = self.allPossibleFBT(left_count)
            right_trees = self.allPossibleFBT(right_count)

            # Backtrack
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        
        return res