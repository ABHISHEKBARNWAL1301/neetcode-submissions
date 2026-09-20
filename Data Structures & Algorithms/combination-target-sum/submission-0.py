class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        def dfs(start, target):
            if target == 0:  
                res.append(list(candidate))
            for i in range(start, n):  
                if (target - nums[i]) >= 0:
                    candidate.append(nums[i])
                    dfs(i, target - nums[i])
                    candidate.pop()
        
        res, candidate = [], []
        n = len(nums)
        dfs(0, target)
        return res

