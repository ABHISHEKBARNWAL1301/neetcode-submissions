class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        l = len(self.arr)
        if l%2 != 0:
            return self.arr[l//2]
        else:
            return (self.arr[l//2] + self.arr[(l-1)//2])/2
        