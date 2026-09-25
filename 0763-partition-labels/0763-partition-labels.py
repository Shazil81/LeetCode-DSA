class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Greedy based ek hashmap me sare values ka index store kr lenge fir chack kr lenge ki wo kha tk gya hai
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i
        
        res = []
        end = size = 0

        for i, char in enumerate(s):
            size += 1

            end = max(end, last_index[char])

            if i == end:
                res.append(size)
                size = 0
        
        return res