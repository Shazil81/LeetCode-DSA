class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x//2

        while left <= right: # hm last value x//2 use kiye kyun ki uske aage sqrt se zyada hoga
            mid = (left + right)//2
            square = mid * mid

            if square == x:
                return mid
            
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
