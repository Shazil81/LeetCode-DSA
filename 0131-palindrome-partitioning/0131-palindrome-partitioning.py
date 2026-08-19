class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def solve(self, index, subset, res, s):
        # base case
        if index >= len(s):
            res.append(subset.copy())
            return
        
        for i in range(index, len(s)):
            substr = s[index:i+1]  # ye prefix bnayega
            if self.isPalindrome(substr): # us prefix ko check krenge
                subset.append(substr) # agar palindrome hai to add
                self.solve(i+1, subset, res, s) # fir recursively call
                subset.pop() # backtrack kr denge

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.solve(0, [], res, s)
        return res