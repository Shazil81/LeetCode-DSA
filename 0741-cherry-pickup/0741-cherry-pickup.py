class Solution:
    def solve(self, r1, c1, r2, c2, grid, n, dp):
        # bahar nikal gaye to invalid
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return float('-inf')

        # thorn (-1) mil gaya to invalid
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')

        # dono end par pahunch gaye
        if r1 == n - 1 and c1 == n - 1 and r2 == n - 1 and c2 == n - 1:
            return grid[r1][c1]

        # memo check
        if dp[r1][c1][r2][c2] != -1:
            return dp[r1][c1][r2][c2]

        # is step ki cherries
        cherries = grid[r1][c1]
        if r1 != r2 or c1 != c2:          # dono alag cell par hain
            cherries += grid[r2][c2]      # same cell ho to double count na ho

        best = max(
            self.solve(r1 + 1, c1, r2 + 1, c2, grid, n, dp),   # dono down
            self.solve(r1 + 1, c1, r2, c2 + 1, grid, n, dp),   # 1 down, 2 right
            self.solve(r1, c1 + 1, r2 + 1, c2, grid, n, dp),   # 1 right, 2 down
            self.solve(r1, c1 + 1, r2, c2 + 1, grid, n, dp),   # dono right
        )

        dp[r1][c1][r2][c2] = cherries + best
        return dp[r1][c1][r2][c2]

    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = [[[[-1] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
        ans = self.solve(0, 0, 0, 0, grid, n, dp)
        return max(0, ans)