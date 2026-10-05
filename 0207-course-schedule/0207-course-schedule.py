from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topo sort wala logic hai (Kahn's Algorithm use hoga)
        # cycle rhega to nhi hoga 
        # BFS (Kahn's Algorithm) Indegrees pe based hai
        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegrees[u] += 1  # indegrees badhaya
        queue = deque()
        res = []
        
        for i in range(numCourses):
            # jiska indegrees 0 hai usko pehle queue me add krenge
            if indegrees[i] == 0:
                queue.append(i)
                
        while len(queue) != 0:
            curr_node = queue.popleft()
            res.append(curr_node)  # res me add kr rhe h kyun ki jiska indegree 0 wo pehle aayega
                
            for adjNode in adj_list[curr_node]:
                # jaise hi adjNode pe phonche uska indegree ghataya
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0: # agar indegree zero hua to add
                    queue.append(adjNode)
        # ye hai to topo sort ka algo lekin topo sort work krta h acyclic directed graph pe
        # or agar acyclic rha to res ka length V k barabar hoga
        if len(res) == numCourses:
            return True
        return False