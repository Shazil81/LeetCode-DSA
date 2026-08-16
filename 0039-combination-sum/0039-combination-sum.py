class Solution:
    def solve(self, index, total, subset, nums, target, res):
        if total == target:
            res.append(subset.copy())
            return
        elif total > target:
            return
        if index >= len(nums):
            return
        curr_sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index, curr_sum, subset, nums, target, res) # yha pe jb hm pick kr rha hain to index ko nhi badha rhe hain kyun ki wohi indez select kr skte hain wapas se
        curr_sum = total
        subset.pop()
        self.solve(index+1, curr_sum, subset, nums, target, res) # jab pick nhi kr rhe h to index ko badha rhe h kyun ki wo wala index ab choose nhi krenge
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        self.solve(0, 0, subset, candidates, target, res)
        return res