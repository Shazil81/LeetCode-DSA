class Solution:
    def dfs(self, node, path, graph, res):
        if node == len(graph)-1:
            res.append(list(path))
            return
        
        for neighbour in graph[node]:
            path.append(neighbour)
            self.dfs(neighbour, path, graph, res)
            path.pop()

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        res = []
        self.dfs(0, [0], graph, res)
        return res
