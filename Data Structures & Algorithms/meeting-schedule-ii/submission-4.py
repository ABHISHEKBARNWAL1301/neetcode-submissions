"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key=lambda x: x.start)
        mp = defaultdict(list)
        for interval in intervals:
            mp[interval.start].append(1)
            mp[interval.end].append(-1)
        
        ans, rooms = 0, 0
        for point in sorted(mp.keys()):
            rooms  += sum(mp[point])
            ans = max(ans, rooms) 
        
        return ans

            

 



        