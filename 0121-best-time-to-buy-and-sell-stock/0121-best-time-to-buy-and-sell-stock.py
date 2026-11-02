class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            mxp = max(profit, mxp)
        return mxp
        