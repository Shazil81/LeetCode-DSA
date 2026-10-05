from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        # Topo sort ka question hai (BFS KAHN's Algo use ho rha hai)
        adj_list = defaultdict(list)
        indegrees = defaultdict(int)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                adj_list[ing].append(recipe)
                indegrees[recipe] += 1
        
        queue = deque(supplies)
        res = []
        recipe_set = set(recipes)

        while queue:
            curr = queue.popleft()
            if curr in recipe_set:
                res.append(curr)
            
            for recipe in adj_list[curr]:
                indegrees[recipe] -= 1

                if indegrees[recipe] == 0:
                    queue.append(recipe)
        
        return res
