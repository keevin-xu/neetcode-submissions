class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        s = newInterval[0]
        e = newInterval[1]
        out = []
        i = intervals
        overlap = False
        if i[0][0] > newInterval[1]:
            out.append(newInterval)
        for j in range(len(intervals)):
            if (i[j][0] <= e and i[j][0] >= s) or (i[j][1] >= s and i[j][1] <= e):
                overlap = True
            else:
                if overlap:
                    out.append([s,e])
                    overlap = False
            if not overlap:
                out.append(i[j])
                if i[j][1] < s and (j + 1) < len(i) and i[j+1][0] > e:
                    out.append(newInterval)
            else:
                e = max(e, i[j][1])
                s = min(s, i[j][0])
        if overlap:
            out.append([s,e])
        elif not overlap and intervals[-1][1] < s:
            out.append(newInterval)
        return out

