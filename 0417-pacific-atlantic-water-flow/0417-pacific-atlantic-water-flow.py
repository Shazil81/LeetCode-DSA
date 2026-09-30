class Solution:
    def dfs(self, r, c, ocean, prev_height, heights):
        m , n = len(heights), len(heights[0])

        # Boundary Check
        if (r < 0 or r >= m or c < 0 or c >= n or ocean[r][c] or heights[r][c] < prev_height):
            return
        
        ocean[r][c] = True

        self.dfs(r+1, c, ocean, heights[r][c], heights)
        self.dfs(r-1, c, ocean, heights[r][c], heights)
        self.dfs(r, c+1, ocean, heights[r][c], heights)
        self.dfs(r, c-1, ocean, heights[r][c], heights)

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m , n = len(heights), len(heights[0])

        atlantic = [[False]*n for _ in range(m)]
        pacific = [[False]*n for _ in range(m)]

        # Pacific k liye or Atlantic k liye (rows se traversal)
        for c in range(n):
            self.dfs(0, c, pacific, heights[0][c], heights)
            self.dfs(m-1, c, atlantic, heights[m-1][c], heights)
        
        for r in range(m): # column se traversal
            self.dfs(r, 0, pacific, heights[r][0], heights)
            self.dfs(r, n-1, atlantic, heights[r][n-1], heights)
        

        # Coomon wala
        res = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        
        return res


        


