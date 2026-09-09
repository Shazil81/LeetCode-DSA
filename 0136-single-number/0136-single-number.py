class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bit se krna asaan h loop se bhi kr skte hain
        res = 0
        for num in nums:
            res = res ^ num  # kyun ki xor operation duplicates ko htata h
        return res
        
            
          