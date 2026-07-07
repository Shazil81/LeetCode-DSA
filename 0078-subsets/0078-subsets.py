class Solution:
    def help(self, index, subset, nums, res):
        if index >= len(nums):  # base case
            res.append(subset.copy())  # kyun ki copy nhi krenge to null aa jayega delete bhi to kr rhe h
            return
        subset.append(nums[index])
        self.help(index+1, subset, nums, res)  # pick wale ko call diya
        subset.pop()  # jo pick kiya wapas jatae waqt pop kr diya
        self.help(index+1, subset, nums, res)  # ab bina pick wale ko call diya
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursion se bhi hoga or bit se bhi
        # yha pe recursion se krte hain
        subset = []
        res = []
        index = 0
        self.help(index, subset, nums, res)
        return res
