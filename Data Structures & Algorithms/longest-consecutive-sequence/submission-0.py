class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                count +=1
            elif nums[i-1] == nums[i]:
                continue
            else:
                count = 1
            res = max(res, count)
        
        return res
