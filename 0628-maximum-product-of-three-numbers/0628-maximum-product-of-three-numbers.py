class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Logic kya hai ki 
        # Case 1: 3 max numbers +ve (apas me multiply)
        # Case 2: 2 -ve small numbers (max number se multiply)
        # Then max(Case1, Case2)
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')

        for num in nums:
            # Update minimums
            if num <= min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

            # Update maximums
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)