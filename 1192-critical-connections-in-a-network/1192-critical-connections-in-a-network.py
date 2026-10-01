class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        # Step 1: Adjacency list banao
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        dt = [-1] * n
        low = [0] * n
        time = 0
        res = []  # Saare Bridges / Critical Connections store honge
        
        def dfs(u, parent):
            nonlocal time
            dt[u] = low[u] = time
            time += 1
            
            for v in adj[u]:
                if v == parent:
                    continue
                
                if dt[v] != -1:
                    # Back-edge case
                    low[u] = min(low[u], dt[v])
                else:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    # Bridge condition check karo aur edge append karo
                    if low[v] > dt[u]:
                        res.append([u, v])
            

        for i in range(n):
            if dt[i] == -1:
                dfs(i, -1)
        
        return res
        