class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        pre_sum = 0
        res = 0
        mp[0] = 1
        for num in nums:
            pre_sum += num
            res += mp[pre_sum-k]
            mp[pre_sum] += 1

        return res
