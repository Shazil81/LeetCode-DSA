class Solution:
    def toLowerCase(self, s: str) -> str:
        # easy one
        s = list(s)
        for i in range(len(s)):
            if s[i].isupper():
                s[i] = s[i].lower()
        
        return "".join(s)
                