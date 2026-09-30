class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      
      
        def fun(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(fun(i+1), fun(i+2))
            return memo[i]

        
        memo = {}
        return min(fun(0), fun(1))