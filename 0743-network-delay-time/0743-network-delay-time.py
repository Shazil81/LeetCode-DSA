from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Dijkstra's Algo use hoga
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist[i] = k se node i tak ka minimum time
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        heap = [(0, k)] # time, node
        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue
            
            for nxt, w in graph[node]:
                new_time = time + w
                if new_time < dist[nxt]:
                    dist[nxt] = new_time
                    heapq.heappush(heap, (new_time, nxt))
        
        ans = 0
        for i in range(1, n + 1):      
            if dist[i] == float('inf'):    
                return -1
            ans = max(ans, dist[i])  # jo max hoga yaani sare nodes ko phonch jayega

        return ans


