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
# why does tracking by earliest end time work?
# GREEDY STEP: Reusing the room that frees up the earliest is always optimal because it leaves you with the maximum possible flexibility for all subsequent meetings. 
#^^^FOR THE FUTURE: when you assign an incoming meeting to a room, you want that room to become available again as quickly as possible. 
# because we already sorted meetings by start time, ascending
# can also think as: if earliest end time is invalid, then all other end times are invalid.
                    