class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minm, profit = float(math.inf), 0
        for price in prices:
            minm = min(minm, price)
            profit = max(profit, price-minm)
        
        return profit