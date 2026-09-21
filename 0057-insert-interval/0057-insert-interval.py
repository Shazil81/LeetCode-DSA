class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        n = len(intervals)
        i = 0

        # left part (for sure ki overlap nhi krega)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # mid part jo ki overlap krega
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # res me add krna hoga jo bhi overlap wala modify hua
        res.append(newInterval)

        # last wala part jo ki overlap nhi hoga
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res



        