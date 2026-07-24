# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS lgega bs ek flag lena usi se manipulate krna hai
        res = []
        queue = collections.deque()
        if root is None:
            return res
        queue.append(root)
        reverse = False
    
        while queue:
            level_size = len(queue)
            lst = []
            
            for _ in range(level_size):
               e = queue.popleft()
               lst.append(e.val)

               if e.left:
                queue.append(e.left)

               if e.right:
                queue.append(e.right)
            # agar reverse true hoga to reverse me add krna h
            if reverse:
                res.append(lst[::-1])
            else:
                res.append(lst)
            
            reverse = not reverse
  
        return res
            