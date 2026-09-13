class MedianFinder:

    def __init__(self):
        self.minm = []
        self.maxm = []

    def addNum(self, num: int) -> None:
        if self.minm and num > self.minm[0]:
            heapq.heappush(self.minm, num)
        else:
            heapq.heappush(self.maxm, -num)

        if len(self.minm) > len(self.maxm) + 1:
            val = -1 * heapq.heappop(self.minm)
            heapq.heappush(self.maxm, val)

        if len(self.maxm) > len(self.minm) + 1:
            val = -1 * heapq.heappop(self.maxm)
            heapq.heappush(self.minm, val)


    def findMedian(self) -> float:
        if len(self.minm) == len(self.maxm):
            return (self.minm[0] - 1*self.maxm[0])/2
        elif len(self.minm) > len(self.maxm):
            return self.minm[0]
        else:
            return -self.maxm[0]

        