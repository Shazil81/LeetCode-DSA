class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        n = len(stones)

        # impossible check
        if (n - 1) % (k - 1) != 0:
            return -1

        # prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j] = range i..j ka min cost
        # diagonal (i == j) = 0, wahi base case hai
        dp = [[0] * n for _ in range(n)]

        # length 2 se n tak (length 1 ka cost 0 hai)
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # range ko do hisson me todo (left ek pile banne layak)
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])

                # agar poori range ek pile ban sakti hai, last merge ka cost add
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]