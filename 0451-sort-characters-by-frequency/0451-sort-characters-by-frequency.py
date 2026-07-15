class Solution:
    def frequencySort(self, s: str) -> str:
       # bucket sort : Optimal One
        n = len(s)
        bucket = [[] for i in range(n+1)] # n+1 banane k pichhe ek reason hai ki mera frequesncy 1 baar to aayega hi isi liye 0th index ko hmlog ignore kr denge
        
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # Bucket me hashmap me jo value hoga yaani ki count usko index pe daal rhe h
        for key, value in freq.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket)-1, 0, -1): # last se chala rhe h is liye kyun ki isme jo sab se zyada frequency hoga uska index last me hoga baaki sab khali rhega 
            for ch in bucket[i]:
                res.append(ch*i)
        
        return "".join(res)
                
