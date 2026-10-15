class Solution:
    def solve(self, index, s, dp):
        if index == len(s): # base case ek path mila last tk gye to
            return 1
        
        if s[index] == '0': # agar zero hua to decode nhi hoga
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        # choice 1: Single digit decode krna
        ways = self.solve(index + 1, s, dp)

        # choice 2: Double digit decode krna
        if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
            ways += self.solve(index+2, s, dp)
        
        dp[index] = ways
        return ways
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        return self.solve(0, s, dp)
