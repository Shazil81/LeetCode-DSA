import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # ye question prim's algorithm pe based hai
        visited = set()
        n = len(points)

        total = 0
        min_heap = [(0, 0)]  # val, index

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            
            if i in visited:
                continue
            
            visited.add(i)
            total += cost

            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    val = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (val, j))
        
        return total