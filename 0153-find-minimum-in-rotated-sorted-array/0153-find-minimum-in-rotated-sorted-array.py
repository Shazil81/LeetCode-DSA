class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Optimal Approach bs yha pe ek chiz h ki sorted wala part k against me check krna h whi pe milega zyada chance hai lekin aisa koi zaruri nhi h edge case hai isme 
        n = len(nums)
        low = 0
        high = n-1
        mini = float('inf')
        while low<=high:
            mid = (low+high)//2
            if nums[mid] <= nums[high]:
                mini = min(mini, nums[mid])
                high = mid - 1
            else:
                mini = min(mini, nums[low])
                low = mid + 1
        return mini