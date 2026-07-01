class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Without using Stack

        left_bracket, right_bracket = 0, 0

        for ch in s:
            if ch == '(':
                left_bracket += 1
            elif ch == ')' and left_bracket > 0:
                left_bracket -= 1
            else:
                right_bracket += 1
        
        return left_bracket + right_bracket
            
