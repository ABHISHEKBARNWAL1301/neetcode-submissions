"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals= sorted(intervals, key = lambda x:x.start)
        heap = []
        res = 0

        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end) 
            res = max(res, len(heap))

        return res




        