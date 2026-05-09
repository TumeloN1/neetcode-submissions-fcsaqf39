class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = profit = 0
        buy = prices[l]
        while r != len(prices):
            sell = prices[r]
            if sell > buy:
                profit = max(profit, sell - buy)
            elif buy > sell:
                l = r
                buy = prices[l]
            r += 1
        
        return profit