class Solution:
    def hammingWeight(self, n: int) -> int:
        # count set bit to bs left binary shift lga k kr do
        count = 0
        for i in range(32):
            if n & (1<<i)!=0:
                count+=1
        return count