class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        

        
        def fun(i, M, state):
            if i >= len(piles):
                return 0

            if (i, M, state) in memo:
                return memo[(i, M, state)]
            ans = 0 if state else float(math.inf)
            for X in range(1, 2*M + 1):
                if state:
                    ans = max(ans, sum(piles[i:i+X]) + fun(i+X, max(M, X), 1-state))
                else:
                    ans = min(ans, fun(i+X, max(M, X), 1-state))
            
            memo[(i, M, state)] = ans
            return ans

        memo = {}
        return fun(0, 1, 1)