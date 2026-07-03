class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
       # monotonic stack pe work krega
       n = len(nums)
       ans = [-1] * n
       stack = []
       # loop 2n se circular k liye yaani 2 pass kr rhe h array me
       for i in range(2*n - 1, -1, -1):
        # ye condition use krne se wo 2nd pass wala bhi array access hoga
        while len(stack) != 0 and stack[-1] <= nums[i%n]:
            stack.pop()
        # first pass me hi update hoga
        if i < n:
            if len(stack) != 0:
                ans[i] = stack[-1]
        stack.append(nums[i%n])
       return ans 

        