"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # intervals= sorted(intervals, key = lambda x:x.start)
        # heap = []
        # res = 0

        # for i in intervals:
        #     if heap and i.start >= heap[0]:
        #         heapq.heappop(heap)
        #     heapq.heappush(heap, i.end) 
        #     res = max(res, len(heap))

        # return res

        line = defaultdict(int)
        for i in intervals:
            line[i.start] += 1
            line[i.end] -= 1
        
        sorted_line = dict(sorted(line.items(), key = lambda x:x[0]))

        res = 0
        ans = 0
        for  val in sorted_line.values():
            ans += val
            res = max(res, ans)
        
        return res

            

 



        