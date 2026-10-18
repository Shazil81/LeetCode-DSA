class Solution:
    def solve(self, i, j, dungeon, m, n, dp):
        if i >= m or j >= n:
            return float('inf')

        if i == m - 1 and j == n - 1:
            return max(1, 1 - dungeon[i][j])  # last me to 1 rehna hi chahiye usse kam to nhi chalega 
        
        if dp[i][j] != -1:
            return dp[i][j]

        down = self.solve(i + 1, j, dungeon, m, n, dp)
        right = self.solve(i, j + 1, dungeon, m, n, dp)

        # bs formula ka khel hai
        need = min(down, right) - dungeon[i][j]  # aage ki requirement - room ka effect
        dp[i][j] = max(1, need)  # is liye ki health 1 se kam n ho
        return dp[i][j]
        

    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        # Memoization TLE remove kr dega
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[-1]*(n) for _ in range(m)]
        return self.solve(0, 0, dungeon, m, n, dp)