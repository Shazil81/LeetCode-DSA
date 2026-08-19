class Solution:
    def solve(self, index, res, nums):
        # base case
        if index >= len(nums):
            res.append(nums.copy())
            return
        
        for i in range(index, len(nums)):
            # Swap: Element ko correct position pe lao
            nums[index], nums[i] = nums[i], nums[index]
            # agle index k liye
            self.solve(index+1, res, nums)
            # Backtrack kro
            nums[index], nums[i] = nums[i], nums[index]


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.solve(0, res, nums)
        return res