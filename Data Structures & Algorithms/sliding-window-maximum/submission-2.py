class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, heap = [], []
        for i in range(k):
            heapq.heappush(heap,(-nums[i], i))
        ans.append(heap[0][0]*-1)
        # print(ans)

        for i in range(1,len(nums)-k+1):
            # print(i)
            while heap and heap[0][1] < i:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i+k-1], i+k-1))
            ans.append(heap[0][0]*-1)

        return ans