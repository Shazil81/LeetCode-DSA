class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Pehla logic kya hai ki koi bhi element 3 baar agar aayega to uska bit count 3 baar ho jayega

        ans = 0
        for i in range(0, 32):
            count = 0
            for num in nums:
                if num & (1 << i) != 0:
                    count += 1
            
            if count % 3 != 0:
                ans = ans | (1 << i) # ye mera har wo bit ko jo count me usko add krega 1 left shift kr k
        
        if ans >= 2**31: # bit k liye signed agar negative rhega to
            ans -= 2**32

        return ans