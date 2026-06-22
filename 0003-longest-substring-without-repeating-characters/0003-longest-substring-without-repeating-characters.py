class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimal solution by using two pointers
        my_dict = {} # dict use kiya
        left = 0
        right = 0
        maxi = 0
        n = len(s)
        while right < n:
            if s[right] in my_dict:
                # agar mera dict me hoga to hm kya krenge ki left ko jha pe mila h us index se ek aage badha denge
                # ek edge case kya hai max lene ka ki ho skta h ki pehle se ho dict me lekin left wha pe nhi ho to kya hoga ki window to valid hoga is liye max lena h left ka or jha pe aaya hai wha pe se ka aage ka index ka 
                left = max(left, my_dict[s[right]]+1)
            # two pointers me right-left+1 ek window length ho jata h  
            maxi = max(maxi, right-left+1)
            my_dict[s[right]] = right # dict me index ko store kr dena
            right+=1
        return maxi

