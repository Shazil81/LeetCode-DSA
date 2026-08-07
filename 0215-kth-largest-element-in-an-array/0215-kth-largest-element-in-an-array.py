class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        n = len(nums)
        # K length ka daal do heap me wo min heap bna lega by default
        for i in range(k):
            heapq.heappush(ans, nums[i])
        # ab k se n chala k check krna h elements ko
        for i in range(k, n):
            # by default to mera min heap bnega yaani kya hoga ki jo top rhega yaani 0th
            # index pe wo mera sab se min rhega or pop bhi wohi hoga
            if nums[i] > ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans, nums[i])
        # k ka length jo hai utna ans me hoga element lekin jo kth largest hoga wo top pe hoga yaani 0th index pe
        return ans[0]

        