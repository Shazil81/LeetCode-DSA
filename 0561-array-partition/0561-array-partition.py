class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort kr do fir 2 ka pair le lo
        total = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            total += nums[i]
        
        return total