class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def fun(start):
            res.append(list(path))
            for i in range(start, n):
                path.append(nums[i])
                fun(i+1)
                path.pop()

        
        res, path = [], []
        n = len(nums)
        fun(0)
        return res

