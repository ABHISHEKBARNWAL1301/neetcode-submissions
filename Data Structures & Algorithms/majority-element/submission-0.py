class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums) // 2]

        # Boyer-Moore Voting Algorithm
        candidate, count = 0,  0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate
