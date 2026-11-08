class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        count = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '-': # dash aane par skip
                continue
            
            if count == k:  # count jab k ho jaye to dash add and count reset
                res += '-'
                count = 0 
            
            res += s[i].upper()
            count += 1
        
        return res[::-1]
