class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Prefix array use hoga
        n = len(arr)
        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        res = []
        for left, right in queries:
            res.append(prefix[right+1] ^ prefix[left])
        
        return res
