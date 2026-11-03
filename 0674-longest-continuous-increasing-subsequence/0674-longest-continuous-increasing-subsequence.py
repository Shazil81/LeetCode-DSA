class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        # Continous Subsequence ka matlab hua subarray
        # Sliding window use hoga
        n = len(nums)
        left = 0
        res = 1
        maxi = 1
        for right in range(1, n):
            if nums[right] > nums[left]:
                res += 1
            else:
                res = 1
            maxi = max(maxi, res)
            left += 1
        
        return maxi
        