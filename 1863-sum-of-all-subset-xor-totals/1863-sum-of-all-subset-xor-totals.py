class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # ye ek formula based question hai
        n = len(nums)

        or_all = 0
        for num in nums:
            or_all |= num
        
        return or_all * (1 << (n - 1))  # or of all elements * 2 ^(n-1)