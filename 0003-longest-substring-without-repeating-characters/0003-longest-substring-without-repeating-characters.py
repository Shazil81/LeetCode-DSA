class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force
        maxi = 0
        n = len(s)
        for i in range(n):
            my_set = set()
            for j in range(i, n):
                if s[j] in my_set:
                    break
                maxi = max(maxi, j-i+1) # sliding window me ek technique hai j-i+1 ek window ka length hota h waise
                my_set.add(s[j])
        return maxi

