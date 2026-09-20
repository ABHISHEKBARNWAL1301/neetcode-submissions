class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort( key = lambda x : x[1])
        numNonOverlapInterval = 0
        lastEnd = float(-math.inf)

        for s, e in intervals:
            if s >= lastEnd:
                numNonOverlapInterval += 1
                lastEnd = e
        
        return len(intervals) - numNonOverlapInterval
