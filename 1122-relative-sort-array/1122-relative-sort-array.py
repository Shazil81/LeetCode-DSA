class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # Counting Sort pe based hai
        freq = {}
        res = []
        for num in arr1: # maine jitne the pehle unhe count kiya
            freq[num] = freq.get(num, 0) + 1
        
        for num in arr2: # fir usi order me unke values ko kiya
            res.extend([num] * freq[num])
            del freq[num]

        for num in sorted(freq): # bache hue values ko add kr diya
            res.extend([num] * freq[num])

        return res
        
        
