class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        # Dijkstra Algorithm se hua hai
        m = len(grid)
        n = len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        heap = []

        # Pehli row ke saare cells se start kar sakte hain
        for c in range(n):
            dist[0][c] = grid[0][c]
            heapq.heappush(heap, (grid[0][c], 0, c))

        while heap:
            cost, r, c = heapq.heappop(heap)

            if cost > dist[r][c]:
                continue

            if r == m - 1:
                return cost

            val = grid[r][c]

            # Neeche wali row ke har column me ja sakte hain
            for nc in range(n):
                new_cost = cost + moveCost[val][nc] + grid[r + 1][nc]

                if new_cost < dist[r + 1][nc]:
                    dist[r + 1][nc] = new_cost
                    heapq.heappush(heap, (new_cost, r + 1, nc))

        return -1