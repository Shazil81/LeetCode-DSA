# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # jo node delete krna hai uske sab se right me dhundhega
    # kyun ki hmko sab se right me add kr dena hai us subtree k
    def findLastRight(self, node):
        while node.right is not None:
            node = node.right
        return node
    def deletion(self, node):
        # 1. edge case ki us node k left me None hua to right se direct connect kro
        if node.left is None:
            return node.right
        # 2. edge case ki us node k right me None hua to node k left se direct connect kro 
        elif node.right is None:
            return node.left
        else:
            # jo node delete krna h uska right hmko dega kyun ki whi right subtree ko hmko left subtree k last me right me add kr dena hai
            right_child = node.right
            # ye last right dega jo node ko delete krna h uske left se
            last_right = self.findLastRight(node.left)
            # ye last right k right me add kr dega node k right subtree ko
            last_right.right = right_child
            return node.left
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1. Base condition
        if root is None:
            return None
        # 2. Base condition
        if root.val == key:
            return self.deletion(root)
        curr = root
        while curr:
            # Searching then deleting
            if curr.val < key:
                if curr.right is not None and curr.right.val == key:
                    curr.right = self.deletion(curr.right)
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is not None and curr.left.val == key:
                    curr.left = self.deletion(curr.left)
                    break
                else:
                    curr = curr.left
        return root 
                
