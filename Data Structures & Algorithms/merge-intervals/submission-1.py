class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        out = []

        intervals.sort(key=lambda x: x[0])
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            if (intervals[i][0] >= s and intervals[i][0] <= e) or (intervals[i][1] >= s and intervals[i][1] <= e):
                s = min(intervals[i][0], s)
                e = max(intervals[i][1], e)
            else:
                out.append([s, e])
                s = intervals[i][0]
                e = intervals[i][1]
        out.append([s, e])

        return out
