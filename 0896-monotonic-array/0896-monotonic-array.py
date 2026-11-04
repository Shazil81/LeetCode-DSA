class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        # Two flag approaches is the best one
        n = len(nums)
        if n == 1:
            return True
        
        is_inc = True
        is_dec = True

        for i in range(1, len(nums)):
            if not is_inc and not is_dec:
                return False

            if nums[i] > nums[i-1]:
                is_dec = False
            if nums[i] < nums[i-1]:
                is_inc = False
        
        return is_inc or is_dec

