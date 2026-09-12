class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1. HashMap 
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        # #2. Heap
        # mp = defaultdict(int)
        # for num in nums:
        #     mp[num] += 1
        
        # heap = []
        # for key, val in mp.items():
        #     if len(heap) == k and  heap[0][0] < val:
        #         heapq.heappop(heap)
        #     heapq.heappush(heap, (val, key))
        
        # ans = []
        # for i in range(k):
        #     ans.append(heap[0][1])
        #     heapq.heappop(heap)

        # return ans
        

        # 3. bucket sort 
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1

        bucket = [[] for i in range(len(nums)+1)]
        for num, count in mp.items():
            bucket[count].append(num)
        
        ans = []
        for arr in bucket[::-1]:
            for num in arr:
                ans.append(num)
                if len(ans) == k:
                    return ans




