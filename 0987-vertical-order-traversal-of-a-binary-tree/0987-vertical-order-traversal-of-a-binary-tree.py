# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base step
        if root is None:
            return []
        
        res = []
        queue = collections.deque()
        # ye special hai
        dict_map = defaultdict(list)
        queue.append((root, 0, 0))
        
        while queue:
            e, row, col = queue.popleft()
            # col key ho jayega or wha pe values (row, value) store ho jayega
            dict_map[col].append((row, e.val))
            # ye to diya hua hai question me
            if e.left:
                queue.append((e.left, row+1, col-1))
            if e.right:
                queue.append((e.right, row+1, col+1))
        # ye step dict_map me col ko sort kr rha h
        for value in sorted(dict_map.keys()):
            # or ye step values ko sort kr rha h agar row khi pe same ho jaye to
            # ye ek list rhega jisme tuples hain
            column_nodes = sorted(dict_map[value])
            temp_lst = []
            # sorted me se temporary me store kra rhe hain
            for row, val in column_nodes:
                temp_lst.append(val)
            res.append(temp_lst)

        return res
            
