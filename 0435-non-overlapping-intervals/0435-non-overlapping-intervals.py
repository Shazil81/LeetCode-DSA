class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # N meetings wala logic lgega
        # last value k based pe sort kr diya
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        count = 1
        prev_end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= prev_end:
                count += 1
                prev_end = intervals[i][1]
        
        return n-count
