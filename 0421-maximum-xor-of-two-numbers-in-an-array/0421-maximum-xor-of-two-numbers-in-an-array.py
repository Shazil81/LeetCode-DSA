class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        max_xor = 0

        for i in range(30, -1, -1):
            # STEP 1: Mask Update
            mask = mask | (1 << i)
            
            # STEP 2: Prefixes Collection
            prefixes = {num & mask for num in nums}
            
            # STEP 3: Target Guess (Greedy)
            candidate = max_xor | (1 << i)
            
            # STEP 4: Verification (A ^ C = B)
            for prefix in prefixes:
                if (prefix ^ candidate) in prefixes:
                    max_xor = candidate
                    break
        
        return max_xor
        