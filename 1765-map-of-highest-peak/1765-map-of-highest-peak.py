from collections import deque
class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        # question me ye keh rha h ki 1 se zero kitna nearest distance pe hai (BFS)
        rows, cols = len(isWater), len(isWater[0])
        vis = [[0] * cols for _ in range(rows)]
        distance = [[0] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:  # hm kya kr rhe h ki one ko find kr k wha se zero ka distance nikal rhe h
                    queue.append((r,c,0)) # source hai isi liye zero add kiya
                    vis[r][c] = 1
        while len(queue) != 0:
            i, j, d = queue.popleft()
            distance[i][j] = d
            for x, y in [(-1,0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                    continue
                if vis[new_i][new_j] == 1:
                    continue
                # ek distance badha do bs or coordinates add krdo
                queue.append((new_i, new_j, d + 1))
                vis[new_i][new_j] = 1
        return distance