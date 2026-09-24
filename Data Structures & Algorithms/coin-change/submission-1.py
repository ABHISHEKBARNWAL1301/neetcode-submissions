class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        def helper(idx, amount):
            if idx == len(coins):
                if amount == 0:
                    return 0
                else:
                    return float(math.inf)

            if (idx, amount) in memo:
                return memo[(idx, amount)]

            take = float(math.inf)

            if amount - coins[idx] >= 0:
                take = 1 + helper(idx, amount - coins[idx])

            not_take = helper(idx+1, amount)

            memo[(idx, amount)] = min(take, not_take)
            return memo[(idx, amount)]

        memo = {}
        ans = helper(0, amount)
        return -1 if ans == float(math.inf) else ans