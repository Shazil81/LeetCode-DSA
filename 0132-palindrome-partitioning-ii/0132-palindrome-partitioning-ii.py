class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def solve(self, index, s, dp):
        n = len(s)
        if index >= n: # agar index end tk phuncha to zero cuts hoga
            return 0
        
        if self.isPalindrome(s[index:n]):  # jo substring hai wo palindrome hai to zero cuts
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        min_cuts = float('inf')
        for i in range(index, n):
            if self.isPalindrome(s[index:i+1]):  # prefix palindrome check
                cuts = 1 + self.solve(i+1, s, dp)   # ek cut lga
                min_cuts = min(cuts, min_cuts)
        
        dp[index] = min_cuts
        return dp[index]

    def minCut(self, s: str) -> int:
        dp = [-1] * (len(s))
        return self.solve(0, s, dp)