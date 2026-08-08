class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window + monotonic deque decreasing size
        dq = deque()
        n = len(nums)
        res = []

        for i in range(n):
            # ye window track krega ki window bada to nhi ho gya n agr hua to pop krega index ko
            if dq and dq[0] < i-k+1:
                dq.popleft()
            # jab koi bada element aayega to usse chhote wale sare ko pop kr do (indices)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            # jab window full hua to max jo hoga wo top wala hi hoga
            if i >= k-1:
                res.append( nums[dq[0]])
        return res
