class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Backtracking ka use hua hai
        # base case
        total_sum = sum(nums) 
        if total_sum % k != 0: # agar total sum k se divide nhi hoga to false
            return False
        
        target = total_sum // k  # ek target le k chalna zaruri hai pair bnega
        nums.sort(reverse=True)
        if nums[0] > target: # agar sort krne k baad pehla digit bada hai yaani ki fit ab nhi hoga to return False
            return False
        
        buckets = [0] * k  # bucket bnao
        
        def help(index):
            if index == len(nums): #base case sare elements fit ho gye hai
                return True
            
            for i in range(k): 
                if buckets[i] + nums[index] <= target:  # agar fit hone layak hai to
                    buckets[i] += nums[index]

                    if help(index+1): # explore agara aage bhi fit hoga to
                        return True
                    
                    buckets[i] -= nums[index]  # backtrack
                
                if buckets[i] == 0:  # agar bucket khali hua to 
                    break
            
            return False
        
        return help(0)