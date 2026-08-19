class Solution:
    def solve(self, index, subset, res, nums, total):
        if total == 0: # base case jab total zero ho kyun ki target ko total le k minus kr rhe h nums k elemnts se
            res.append(subset.copy())
            return
        if total < 0:
            return 
        if index >= len(nums):
            return
        
        for i in range(index, len(nums)): # looping ka use hai recursion me
            if i > index and nums[i] == nums[i-1]: # ye condition duplicates ko skip krne k liye hai
                continue
            subset.append(nums[i])
            self.solve(i+1, subset, res, nums, total - nums[i])
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort() # sort kr k kaam hoga ye approach me
        self.solve(0, subset, res, candidates, target)
        return res