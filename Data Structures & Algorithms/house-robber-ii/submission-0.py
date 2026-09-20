class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob1(nums):
            if len(nums) == 1:
                return nums[0]

            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            

            for i in range(2, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

            return dp[n-1]

        n = len(nums)
        if n == 1:
            return nums[0]
        x = rob1(nums[:n-1])
        y = rob1(nums[1:])
        return max(x, y)
