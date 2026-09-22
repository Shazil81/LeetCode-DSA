class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy algorithm
        jump = left = right = 0
        n = len(nums)
        while right < n -1:
            farthest = 0
            # jo left chal rha h wo minimum hai or right max
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])
            left = right+1
            right = farthest
            jump+=1 
        return jump