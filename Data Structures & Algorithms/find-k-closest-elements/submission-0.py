class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        for elem in arr:
            diff = abs(elem - x)
            item = (-diff, -elem)

            if len(heap) < k:
                heapq.heappush(heap, item)
            elif item > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, item)
                
        ans = [-elem[1] for elem in heap]
        return sorted(ans)

