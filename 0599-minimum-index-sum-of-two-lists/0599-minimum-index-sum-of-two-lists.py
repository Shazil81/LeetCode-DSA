class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Step 1: list1 ke names ko unke my_map ke saath map me daalo
        my_map = {}
        for i in range(len(list1)):
            my_map[list1[i]] = i

        mini = float('inf')
        res = []

        # Step 2: list2 pe loop chalao aur map me check karo
        for j in range(len(list2)):
            name = list2[j]
            if name in my_map:
                s = my_map[name] + j
                if s < mini:
                    mini = s
                    res = [name]       # naya best, reset
                elif s == mini:
                    res.append(name)   # tie
        return res