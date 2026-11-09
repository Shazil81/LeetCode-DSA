class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        for ch in s:
            if ch in odd:
                odd.remove(ch)   # pair ban gaya
            else:
                odd.add(ch)      # abhi akela hai

        # odd me jitne letters bache, wo bina pair ke hain
        if len(odd) > 0:
            return len(s) - len(odd) + 1
        return len(s)