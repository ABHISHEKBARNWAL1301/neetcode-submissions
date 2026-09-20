class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums.sort()
        # count = 1
        # res = 1
        # for i in range(1, len(nums)):
        #     if nums[i-1]+1 == nums[i]:
        #         count +=1
        #     elif nums[i-1] == nums[i]:
        #         continue
        #     else:
        #         count = 1
        #     res = max(res, count)
        
        # return res

        seen = set(nums)
        res = 0
        for num in nums:
            count = 0
            if num + 1 not in seen:
                while num in seen:
                    count += 1
                    num -= 1
            res = max(res, count)
        return res


