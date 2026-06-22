class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        n = len(s)
        for i in range(n):
            if i<n-1 and letters[s[i]] < letters[s[i+1]]: # agar chhota value pehle aata h to usko minus kr denge bs wohi condition diya hua h
                res-=letters[s[i]]
            else:
                res+=letters[s[i]]
        return res