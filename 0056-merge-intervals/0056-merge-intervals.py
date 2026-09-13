class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        res = []
        for i in range(1,n):
            if intervals[i][0] <= curr_end:
                curr_end = max(intervals[i][1], curr_end)
            else:
                res.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
        res.append([curr_start, curr_end])
        return res
