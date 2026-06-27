class Solution:
    # Lower Bound Code for first occurence
    def lowerBound(self, nums, target):
        lb = -1
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    # Upper Bound code for last occurrence
    def upperBound(self, nums, target):
        ub = -1
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target) # calling Lower Bound
        if lb == -1 or nums[lb]!= target: # checking if the target is not in the nums
            return [-1, -1]
        ub = self.upperBound(nums, target) # calling Upper bound

        if ub == -1:
            return [lb, len(nums) - 1]

        return [lb, ub - 1]