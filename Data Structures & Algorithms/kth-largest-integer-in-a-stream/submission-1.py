class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.klarge = []
        for num in nums:
            if len(self.klarge) == k:
                if num > self.klarge[0]:
                    heapq.heapreplace(self.klarge, num)
            else:
                heapq.heappush(self.klarge, num)

    def add(self, val: int) -> int:
        if len(self.klarge) == self.size:
            if val > self.klarge[0]:
                heapq.heapreplace(self.klarge, val)
        else:
            heapq.heappush(self.klarge, val)

        return self.klarge[0]
        
