"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end]
        heapq.heapify(rooms)

        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i].end)
        return len(rooms)

                    