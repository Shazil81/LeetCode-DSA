class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pv == pu:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # Minimum spanning Tree ka question hai bs wo edge btana hai jo bekar hai yaani uske htane pe minimum spannig tree bna rhe mera or agar waisa kai edge hai to last wala hi dena hai
        res = 0
        n = len(edges)
        ds = DisjointSet(n)
        for u, v in edges:
            if not ds.Union(u, v):  # jo same me hoga wohi redundant edge hoga
                res = [u, v]
        
        return res