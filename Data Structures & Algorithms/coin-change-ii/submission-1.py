class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def fun(i,amount):
            if i == len(coins):
                if amount==0:
                    return 1
                return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            take = 0
            if amount-coins[i]>=0:
                take = fun(i,amount-coins[i])
            nottake = fun(i+1,amount)

            memo[(i, amount)] = take + nottake
            return memo[(i,amount)]

        memo = {}
        return fun(0, amount)