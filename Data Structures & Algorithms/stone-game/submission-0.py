class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def fun(i, j):
            if i>j:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            

            memo[(i, j)] = max(piles[i], piles[j]) + min(fun(i+1, j), fun(i, j-1))

            return memo[(i, j)]

        total = sum(piles)
        memo = {}
        alice = fun(0, len(piles)-1)
        return alice > total - alice