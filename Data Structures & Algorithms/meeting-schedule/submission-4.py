"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        sort_list= sorted(intervals, key = lambda x : x.start)

        l1 = [sort_list[0]]

        for i in range(1,len(sort_list)):
            if l1[-1].end > sort_list[i].start:
                return False
            else:
                l1.append(sort_list[i])
        if len(sort_list) == len(intervals):
            return True

         