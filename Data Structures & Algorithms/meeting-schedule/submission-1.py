"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 1:
            return True
        for i in range(1, len(intervals)):
            bef = intervals[i-1]
            curr = intervals[i]
            if (curr.start > bef.start and curr.start < bef.end) or (curr.end > bef.start and curr.end < bef.end) or (bef.start >= curr.start and bef.end <= curr.end):
                return False
        return True