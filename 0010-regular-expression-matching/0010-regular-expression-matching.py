class Solution:
    def solve(self, i, j, s, p, dp):
        if i >= len(s) and j >= len(p):
            return True

        if j >= len(p):
            return False 
        
        if dp[i][j] != -1:
            return dp[i][j]
 
        match = i < len(s) and  (s[i] == p[j] or p[j] == '.')
        if (j+1) < len(p) and p[j+1] == '*':
            ans = (self.solve(i, j+2, s, p, dp) or (match and self.solve(i+1, j, s, p, dp)))
        
        elif match:
            ans = self.solve(i+1, j+1, s, p, dp)
        
        else: 
            ans = False
        
        dp[i][j] = ans
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return self.solve(0, 0, s, p, dp)