class Solution:

    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(n+1)]

        for index in range(n-1, -1, -1):
            for buy in range(0, 2):
                if buy == 1:
                    buy_ = -prices[index] + dp[index+1][0]
                    not_buy = 0 + dp[index+1][1]
                    profit = max(buy_, not_buy)
                else:
                    sell = prices[index] - fee + dp[index+1][1]
                    not_sell = 0 + dp[index+1][0]
                    profit = max(sell, not_sell)
                
                dp[index][buy] = profit
        
        return dp[0][1]


        