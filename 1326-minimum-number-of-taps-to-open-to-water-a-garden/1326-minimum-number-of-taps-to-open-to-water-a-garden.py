class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        maxReach = [0] * (n + 1)
        for i in range(n + 1):
            left_bound = max(0, i - ranges[i])
            right_bound = min(n, i + ranges[i])
            maxReach[left_bound] = max(maxReach[left_bound], right_bound)
        
        # Jump Game 2 starts from here
        taps = left = right = 0
        while right < n:
            farthest = 0
            # jo left chal rha h wo minimum hai or right max
            for i in range(left, right + 1):
                farthest = max(farthest, maxReach[i])
            
            if farthest <= right:
                # koi progress nahi, matlab pura garden cover nahi ho sakta
                return -1
            
            left = right + 1
            right = farthest
            taps += 1
        
        return taps
        
