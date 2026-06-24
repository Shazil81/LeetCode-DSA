class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # This is optimal approach two pointers
        n = len(nums)
        left = 0
        right = 0
    	
        while right < n:
    	    # jaise hi right pointer non zero pe phonchega tb swap or left += 1
    	    if nums[right] != 0:
    	        nums[right], nums[left] = nums[left], nums[right]
    	        left += 1
    	    right += 1 
        