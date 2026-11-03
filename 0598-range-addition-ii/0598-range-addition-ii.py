class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_row = m
        min_col = n
        # Jo area overlap krega wohi max hoga (minimum hi wala overlap krega)
        # To formula yhi hota hai product of min_row and min_col
        for r, c in ops:
            min_row = min(min_row, r)
            min_col = min(min_col, c)
            
        return min_row * min_col