class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)  # last bit ko res me add kr de rhe h or usko left shift kr de rhe h ek baar taki jagah khali rhe agle last k liye
            n >>= 1  # n me se ek bit hta de rhe h taaki last bit second last wala ban jaye
        
        return res