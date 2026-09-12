class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base Case
        if n == 1:
            return "0"
        
        # Length and middle
        l = (1 << n) - 1  # 2^n - 1
        mid = l // 2 + 1  # 2 ^ (n - 1)

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n-1, k)
        
        else:
            # Mirror position in left half
            mirror = l - k + 1
            original_bit = self.findKthBit(n - 1, mirror)
            # Inverting It
            if original_bit == "0":
                return "1"
            else:
                return "0"
            
        
        