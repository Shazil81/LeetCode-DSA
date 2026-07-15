class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort : Optimal One
        n = len(nums)
        bucket = [[] for i in range(n+1)] # n+1 banane k pichhe ek reason hai ki mera frequesncy 1 baar to aayega hi isi liye 0th index ko hmlog ignore kr denge
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # Bucket me hashmap me jo value hoga yaani ki count usko index pe daal rhe h
        for key, value in freq.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket)-1, 0, -1): # last se chala rhe h is liye kyun ki isme jo sab se zyada frequesncy hoga uska index last me hoga baaki sab khali rhega 
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
