import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # Dijkstra Algorithm based (heapq)
        rows = len(grid)
        cols = len(grid[0])
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = grid[0][0]
        pq =[]
        heapq.heappush(pq, [grid[0][0], 0, 0])
        while pq:
            eff, i, j = heapq.heappop(pq)
            if i == rows - 1 and j == cols - 1:
                return eff
            if eff > effort[i][j]:
                continue

            for x, y in [[-1,0], [0,-1], [1,0], [0,1]]:
                new_i, new_j = i+x, j+y
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                new_eff = max(eff, grid[new_i][new_j])
                if new_eff < effort[new_i][new_j]:
                    effort[new_i][new_j] = new_eff
                    heapq.heappush(pq, [new_eff, new_i, new_j])