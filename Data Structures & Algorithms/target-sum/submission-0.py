class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    



        def fun(idx, target)->int:
            if idx == len(nums):
                if target == 0:
                    return 1
                return 0
            if (idx, target) in memo:
                return memo[(idx, target)]

            take = fun(idx+1, target - nums[idx])
            take_neg = fun(idx+1, target + nums[idx])

            memo[(idx, target)] =  take + take_neg
            return memo[(idx, target)]

        memo = {}
        return fun(0, target)