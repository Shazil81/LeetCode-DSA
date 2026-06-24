class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag Algorithm (most optimal for this problem)
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            # low ko 0 k liye use krenge
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # mid ko 1 k liye rakhe hue h
            elif nums[mid] == 1:
                mid += 1
            # isme 2 k liye use hoga
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums