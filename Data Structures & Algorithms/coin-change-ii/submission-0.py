class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        def fun(idx, amount)->int:
            if idx == len(coins):
                if amount == 0:
                    return 1
                return 0
            if (idx, amount) in memo:
                return memo[(idx, amount)]

            take = 0
            if amount-coins[idx] >= 0:
                take = fun(idx, amount-coins[idx])
            not_take = fun(idx+1, amount)

            memo[(idx, amount)] =  take + not_take
            return memo[(idx, amount)]

        memo = {}
        return fun(0, amount)