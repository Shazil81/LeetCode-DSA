from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Topo Sort ka part + reverse edges of graph
        V = len(graph)
        adj_list = [[] for _ in range(V)]
        indegrees = [0 for _ in range(V)]
        # reverse kr rhe h adeges ko
        for node in range(V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)
                indegrees[node] += 1
        # topo sort ka concept agar indegrees 0 to add
        queue = deque()
        for node in range(V):
            if indegrees[node] == 0:
                queue.append(node)
        # topo sort kahn's algorithm
        res = []
        while len(queue) != 0:
            node = queue.popleft()
            res.append(node)
            for adjNode in adj_list[node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        res.sort()
        return res


                