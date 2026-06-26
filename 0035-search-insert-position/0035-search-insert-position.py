class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This code is of lower bound but lb = len(nums) instead
        low = 0
        high = len(nums) -1
        lb = len(nums)
        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                lb =  mid
                high = mid - 1
            else:
                low = mid + 1
        return lb