class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [1] + [1]*n
        post_prod = [1]*n + [1]
        for i in range(n):
            pre_prod[i+1] = pre_prod[i]*nums[i]
            post_prod[n-(i+1)] = post_prod[n-i]*nums[n-(i+1)]

        ans = []
        # print(pre_prod, post_prod)
        for i in range(n):
            ans.append(pre_prod[i]*post_prod[i+1])
        
        return ans
        
