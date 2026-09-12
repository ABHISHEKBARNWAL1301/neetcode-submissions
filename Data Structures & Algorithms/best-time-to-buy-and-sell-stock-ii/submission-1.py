class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i in range(1, len(prices)):
        #     profit = prices[i] - prices[i-1]
        #     res += profit if profit > 0 else 0
        # return res
        def fun(i, state):
            if i == len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i, state)]
            if state:
                dp[(i, state)] = max(prices[i] + fun(i+1, 1-state), fun(i+1, state))
            else:
                dp[(i, state)] = max(-prices[i] + fun(i+1, 1-state), fun(i+1, state))
            
            return dp[(i, state)]
        
        dp = {}
        return fun(0, 0)