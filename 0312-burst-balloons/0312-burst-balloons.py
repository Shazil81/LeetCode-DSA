class Solution:
    def solve(self, arr, i, j, dp):
        # koi balloon nahi bacha
        if i > j: 
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        max_coins = 0

        for k in range(i, j + 1):
            coins = (self.solve(arr, i, k - 1, dp)
                     + self.solve(arr, k + 1, j, dp)
                     + arr[i-1] * arr[k] * arr[j+1])
            max_coins = max(max_coins, coins)

        dp[i][j] = max_coins
        return max_coins

    def maxCoins(self, nums: list[int]) -> int:
        # MCM pattern bs thoda twist hai
        n = len(nums)
        arr = [1] + nums + [1]  # question me given hai
        dp = [[-1] * (n + 2) for _ in range(n + 2)]  # n+1 bhi kr skte hain
        return self.solve(arr, 1, n, dp) 