class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1

        # Step 1: find krna pivot index ko
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        # Step 2: agar pivot n mile tab
        if pivot == -1:
            nums.reverse()
            return
        

        # Step 3: right side se chhota dhundho
        for j in range(n-1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break
        
        # Step 4: Pivot k baad wala part reverse kr do (ascending krna hai)
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1 

        