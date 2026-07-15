class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        # Moore's Voting algorithm
        count = 0
        major = 0
        for num in arr:
            if count == 0:
                major = num
            if major == num:
                count+=1
            else:
                count-=1
        return major