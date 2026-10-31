class Solution:
    def solve(self, arr, i, j, dp):
        # beech me koi cut nahi
        if j - i <= 1:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        min_cost = float('inf')

        # i aur j ke beech wale har cut ko pehla cut maan ke try karo
        for k in range(i + 1, j):
            cost = (arr[j] - arr[i]
                    + self.solve(arr, i, k, dp)
                    + self.solve(arr, k, j, dp))
            min_cost = min(min_cost, cost)

        dp[i][j] = min_cost
        return min_cost
        
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts.sort()
        arr = [0] + cuts + [n]
        size = len(arr)

        dp = [[-1] * size for _ in range(size)]

        return self.solve(arr, 0, size - 1, dp)