class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        res_index = 0
        
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[idx], nums[res_index] = nums[res_index], nums[idx]
                res_index += 1
            
        return res_index



