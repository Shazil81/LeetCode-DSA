class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # Grid view:
        # Row 0: c  b  a
        # Row 1: d  a  f
        # Row 2: g  h  i

        # Col:   0  1  2
        rows = len(strs)
        cols = len(strs[0])
        count = 0

        for c in range(cols):
            for r in range(rows-1):
                if strs[r][c] > strs[r+1][c]:
                    count += 1
                    break
        
        return count