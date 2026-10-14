class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def Union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pv == pu:
            return True  # ye edge extra hai
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return False  # yaani extra nhi hai edge
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # number of connected components find kr k 1 ghata denge sirf to wohi min number of edges hoga join krne k liye
        ds = DisjointSet(n)
        extra_edges = 0
        for u, v in connections:
            if ds.Union(u, v):
                extra_edges += 1

        components = 0
        for i in range(n):
            if ds.find(i) == i:
                components += 1
        if extra_edges >= components - 1:
            return components - 1
        return -1


