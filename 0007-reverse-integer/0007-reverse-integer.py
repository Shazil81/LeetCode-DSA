class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x = x//10
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res * sign