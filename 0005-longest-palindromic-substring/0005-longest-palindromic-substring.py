class Solution:
    def solve(self, l, r, s):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
       
        return r-l-1
        
    def longestPalindrome(self, s: str) -> str:
        # Approach 2 -> Optimal Solution
        n = len(s)
        start = 0 # jo max len milega uska start
        end = 0 # jo max len milega uska end 

        for i in range(0, n):
            len1 = self.solve(i, i, s)
            len2 = self.solve(i, i+1, s)
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1)//2 # ab start ko upadte krna hai aise ki i se left wala part
                end = i + max_len//2 # ab end ko aise update krna hai ki i se right wala part
        
        return s[start:end+1]

        
        
        