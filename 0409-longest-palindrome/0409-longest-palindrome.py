class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        has_odd = False

        for f in count.values():
            length += (f // 2) * 2   # sirf pairs lo
            if f % 2 == 1:
                has_odd = True       # beech ke liye ek letter available

        if has_odd:
            length += 1

        return length