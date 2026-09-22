class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])

        count = 1
        prev_end = points[0][1]  # pehla arrow first balloon k end pe

        for start, end in points[1 : len(points)]:
            if start > prev_end: # agar start prev_end se bada hai yaani or zarurat hai arrow ki common rehta tab na ek hi arrow me ho jata
                count += 1
                prev_end = end
        
        return count




