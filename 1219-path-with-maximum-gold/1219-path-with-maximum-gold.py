class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # left, right, up down
        # 0 can't visit
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            gold = grid[r][c]
            grid[r][c] = 0

            # 4 directions me jayenge
            best = max(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            )

            grid[r][c] = gold

            return gold + best
        
        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, dfs(r, c))
        
        return max_gold