class Solution:
    def candy(self, ratings: list[int]) -> int:
        # Greedy to hai slope method
        total_candies = 1
        up = down = peak = 0

        for i in range(1, len(ratings)):
            # Agar incresing hai tab
            if ratings[i] > ratings[i-1]:
                up += 1
                down = 0
                peak = up
                total_candies += (up + 1)
            # Agar flat hai tab
            elif ratings[i] == ratings[i-1]:
                up = 0
                down = 0
                peak = 0
                total_candies += 1
            # Agar decresing hai tab
            else:
                up = 0
                down += 1
                total_candies += down 

                if down > peak: # Peak ko maintain krne k liye 
                    total_candies += 1
        
        return total_candies