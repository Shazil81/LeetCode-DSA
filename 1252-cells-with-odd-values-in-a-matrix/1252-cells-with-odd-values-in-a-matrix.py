class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row = [0] * m
        col = [0] * n
        
        # 1. Track kitni baar kaunsi row aur column increment hui
        for r, c in indices:
            row[r] += 1
            col[c] += 1
            
        ans = 0
        
        # 2. Har cell (i, j) ko check karo
        for i in range(m):
            for j in range(n):
                total_val = row[i] + col[j]
                if total_val % 2 != 0:
                    ans += 1
                    
        return ans