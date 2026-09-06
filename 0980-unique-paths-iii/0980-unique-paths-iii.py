class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        start_r, start_c = 0, 0
        empty_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_count += 1
                elif grid[r][c] == 0:
                    empty_count += 1
                elif grid[r][c] == 2:
                    empty_count += 1
        
        self.paths = 0

        def dfs(r, c , remaining):
            # boundary ya obstacle check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or grid[r][c] == -2:
                return
            
            # end cell pe pahunch gaye
            if grid[r][c] == 2:
                # agar saare walkable squares cover ho chuke hain, valid path hai
                if remaining == 0:
                    self.paths += 1
                return   # end se aage nahi jaana (chahe remaining 0 ho ya na ho)
            # current cell ko visited mark karo (temporarily obstacle bana do)
            temp = grid[r][c]
            grid[r][c] = -2  # -2 matlab "is path mein visited"
            
            # 4 directions try karo, remaining ek se kam karke
            dfs(r + 1, c, remaining - 1)
            dfs(r - 1, c, remaining - 1)
            dfs(r, c + 1, remaining - 1)
            dfs(r, c - 1, remaining - 1)
            
            # BACKTRACK: cell ko wapas original value pe restore karo
            grid[r][c] = temp
        
        dfs(start_r, start_c, empty_count - 1) # remaining - 1 is liye kyun ki start cell khud shamil hai

        return self.paths
