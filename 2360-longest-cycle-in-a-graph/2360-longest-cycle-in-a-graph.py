from collections import deque
class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        indegree = [0] * n

        # Step 1: Har node ki indegree calculate krna hai
        for u in range(n):
            if edges[u] != -1:
                indegree[edges[u]] += 1
        
        # Step 2: Jin nodes ki indegree 0 hai unhe me queue me daalna hai
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        # Step 3: Non Cycle nodes ko pura remove kr do
        vis = [False] * n
        while queue:
            node = queue.popleft()
            vis[node] = True
            neighbour = edges[node]

            if neighbour != -1:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        # Step 4: Ab jo nodes unvis hai yaani unka indegree > 0 wo cycles hai
        maxi = -1
        for i in range(n):
            if not vis[i]:
                cycle_len = 0
                curr = i

                while not vis[curr]:
                    vis[curr] = True
                    curr = edges[curr]
                    cycle_len += 1
                
                maxi = max(maxi, cycle_len)
        
        return maxi
        
