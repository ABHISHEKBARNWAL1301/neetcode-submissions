class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_feasible(largest_sum):
            subarray = 1
            curSum = 0
            for num in nums:
                if curSum + num <= largest_sum:
                    curSum += num
                else:
                    subarray +=1
                    curSum = num
            
            return subarray <= k

        l, r  = max(nums), sum(nums)
        res = r
        while l <= r:
            mid  = (l+r)//2
            if is_feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res