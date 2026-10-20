class Solution:
    def solve(self, i, j, s, t, dp):
        # Base Case 1: Agar target string 't' poori khatam ho gayi
        if j == len(t):
            return 1

        # Base Case 2: Agar source string 's' khatam ho gayi par 't' bachi hai
        if i == len(s):
            return 0

        # Check karo agar yeh state pehle se calculated hai
        if dp[i][j] != -1:
            return dp[i][j]

        # Agar characters match karte hain
        if s[i] == t[j]:
            ans = self.solve(i + 1, j + 1, s, t, dp) + self.solve(i + 1, j, s, t, dp)
        else:
            ans = self.solve(i + 1, j, s, t, dp)

        dp[i][j] = ans
        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.solve(0, 0, s, t, dp)