class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: get all xor first
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # Step 2: find righmost set bit
        rm_set_bit = total_xor & (-total_xor)

        # Step 3: divide in two groups and xor each group
        x = 0
        y = 0
        for num in nums:
            if num & rm_set_bit:
                x ^= num
            else:
                y ^= num
        
        return [x, y]
