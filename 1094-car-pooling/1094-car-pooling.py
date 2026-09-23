class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        timeline = [0] * 1001
        for num, start, end in trips:
            timeline[start] += num
            timeline[end] -= num
        
        curr = 0
        for change in timeline:
            curr += change
            if curr > capacity:
                return False
        
        return True