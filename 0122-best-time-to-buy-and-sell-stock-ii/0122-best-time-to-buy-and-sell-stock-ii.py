class Solution:
    def solve(self, index, buy, prices, dp):
        # base case
        n = len(prices)
        if index == n:
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        if buy == 1: # iska mtlb hm khrid skte hain ya nhi
            buy_ = -prices[index] + self.solve(index+1, 0, prices, dp)
            not_buy = 0 + self.solve(index+1, 1, prices, dp)
            profit = max(buy_, not_buy)
        else: # jab buy = 0 hoga tab hm sell krenge yaani nhi kharid skte hain or sell mera man
            sell = prices[index] + self.solve(index+1, 1, prices, dp)
            not_sell = 0 + self.solve(index+1, 0, prices, dp)
            profit = max(sell, not_sell)
        
        dp[index][buy] = profit
        return dp[index][buy]
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1 -> Recursion  (TLE dega)
        # ek baar me kharidenge to doabara nhi kharid skte hain bina beche hue
        dp = [[-1] * 2 for _ in range(len(prices))]
        return self.solve(0, 1, prices, dp)