class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        # monotonic stack pe based hai
        stack = []
        n = len(nums)
        for i in range(n):
            # agar positive hai to add kro stack me
            if nums[i] > 0:
                stack.append(nums[i])
            else:
                # jab negative bada ho jayega to pop krte rehna jab tk positive usse bada na ho jaye
                while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(nums[i]):
                    stack.pop()
                # or agar negative positive barabar ho jayega to bhi pop ho jayega
                if len(stack) != 0 and stack[-1] == abs(nums[i]):
                    stack.pop()
                # ya stack khali hojaye mtlb negative bhut bada ho gya or agar ek baar negative aaya to fir jab negative aayega to add hoga
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(nums[i])
        return stack