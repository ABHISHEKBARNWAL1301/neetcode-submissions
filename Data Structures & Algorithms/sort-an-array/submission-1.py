class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [0]*100001
        OFFSET = 50000
        for num in nums:
            bucket[num + OFFSET] +=1

        ans = []
        for i in range(100001):
            if bucket[i] > 0:
                for j in range(bucket[i]):
                    ans.append(i-OFFSET)
        
        return ans