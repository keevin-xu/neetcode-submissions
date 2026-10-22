class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        out = []

        intervals.sort(key=lambda x: x[0])
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            if (intervals[i][0] <= e):
                s = min(intervals[i][0], s)
                e = max(intervals[i][1], e)
            else:
                out.append([s, e])
                s = intervals[i][0]
                e = intervals[i][1]
        out.append([s, e])

        return out
