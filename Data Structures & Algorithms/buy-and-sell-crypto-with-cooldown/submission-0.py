class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def fun(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i, state)]
                
            if state:
                dp[(i, state)] = max(prices[i] + fun(i+2, 1-state), fun(i+1, state))
            else:
                dp[(i, state)] =  max(-prices[i] + fun(i+1, 1-state), fun(i+1, state))
            
            return dp[(i, state)]
            
        dp = {}
        return fun(0, 0)
