class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR use kr k sare bits ko 1 kr do
        # AND use kr k sare bits ko check kr lo 1 hai kya ki nhi agar nhi hai to altenate bits nhi hoga

        x = n ^ (n >> 1) # sare bits 1 kr dega
        return x & (x + 1) == 0  # sare 1 bits check kr lega