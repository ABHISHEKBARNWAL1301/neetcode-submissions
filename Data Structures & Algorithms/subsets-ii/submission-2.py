class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def fun(i, subset):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                fun(j+1, subset)
                subset.pop()

        
        res = []
        nums.sort()
        fun(0, [])
        return res

