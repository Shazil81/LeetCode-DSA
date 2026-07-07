class Solution:
    def solve(self, index, total, nums):
        if index == 0:
            if total == 0 and nums[0] == 0:
                return 2
            if total == -nums[0] or nums[0] == total: # kyun ki target negative hai to edge case hua
                return 1
            return 0

        add = self.solve(index-1, total + nums[index], nums)
        subtract = self.solve(index-1, total - nums[index], nums)

        return add + subtract

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Recursion se krte hain TLE dega
        n = len(nums)
        return self.solve(n-1, target, nums)