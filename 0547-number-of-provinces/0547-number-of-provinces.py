class Solution:
    def dfs(self, node, isConnected, vis):
        vis[node] = True
        n = len(isConnected)
        for neighbour in range(n):
            if isConnected[node][neighbour] == 1 and not vis[neighbour]:
                self.dfs(neighbour, isConnected, vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Connected Components wala question hai
        count = 0
        n = len(isConnected)
        vis = [False] * n

        for node in range(n):
            if not vis[node]: # har unvis se start krenge dfs call denge dfs check kr lega ki usse kitna connected hai usko wo vis kr dega or wo ek group ya province kehlayega to us pure province ko 1 count krenge
                self.dfs(node, isConnected, vis)
                count += 1
        
        return count