class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # Move zeros to end ka concept us hoga
        n = len(nums)
        if n == 1:
            return nums
        
        i, j = 0, 0
        while j < n:
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
        return nums
