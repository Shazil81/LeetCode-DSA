class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        # 2 condition hoga ya to overlap kre ya to n kre
        count = 0
        n = len(timeSeries)

        for i in range(n-1):
            # No overlap
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                count += duration
            else:
                # Overlap
                count += timeSeries[i+1] - timeSeries[i]
        
        # last wala to hmlog include nhi kr rhe h
        count += duration
        return count
