class Solution:
    def solve(self, prefix, k, i, j, dp):
        # ek pile: cost 0
        if i == j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        res = float('inf')

        # range ko do hisson me todo, left hissa 1 pile banne layak ho
        for m in range(i, j, k - 1):
            res = min(res,
                      self.solve(prefix, k, i, m, dp)
                      + self.solve(prefix, k, m + 1, j, dp))

        # agar poori range ek pile ban sakti hai, to last merge ka cost add
        if (j - i) % (k - 1) == 0:
            res += prefix[j + 1] - prefix[i]

        dp[i][j] = res
        return res


    def mergeStones(self, stones: list[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[-1] * n for _ in range(n)]

        return self.solve(prefix, k, 0, n - 1, dp)