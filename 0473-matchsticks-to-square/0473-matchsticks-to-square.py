class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # base case
        total_sum = sum(matchsticks)
        if total_sum % 4 != 0:
            return False
        
        target = total_sum // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4

        def help(index):
            if index == len(matchsticks):
                return True
            
            curr = matchsticks[index]
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]

                    if help(index+1):
                        return True

                    sides[i] -= matchsticks[index]
                
                if sides[i] == 0:
                    break
            
            return False
        
        return help(0)

