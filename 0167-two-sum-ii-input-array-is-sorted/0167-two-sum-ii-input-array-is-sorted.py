class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        #two pointers use hoga sorted bhi hai
        n = len(arr)
        left = 0
        right = n - 1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1