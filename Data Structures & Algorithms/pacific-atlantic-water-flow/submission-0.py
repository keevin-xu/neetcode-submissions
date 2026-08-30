class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []
        pacific = set()
        atlantic = set()
        def dfshelp(x, y, seen):
            stack = []
            stack.append((x, y))
            seen.add((x, y))
            while stack:
                curr = stack.pop()
                
                # up
                if (curr[0] - 1 >= 0 and heights[curr[0] - 1][curr[1]] >= heights[curr[0]][curr[1]] and not (curr[0] - 1, curr[1]) in seen):
                    seen.add((curr[0] - 1, curr[1]))
                    stack.append((curr[0] - 1, curr[1]))
                # down
                if (curr[0] + 1 < len(heights) and heights[curr[0] + 1][curr[1]] >= heights[curr[0]][curr[1]] and not (curr[0] + 1, curr[1]) in seen):
                    seen.add((curr[0] + 1, curr[1]))
                    stack.append((curr[0] + 1, curr[1]))
                # left
                if (curr[1] - 1 >= 0 and heights[curr[0]][curr[1] - 1] >= heights[curr[0]][curr[1]] and not (curr[0], curr[1] - 1) in seen):
                    seen.add((curr[0], curr[1] - 1))
                    stack.append((curr[0], curr[1] - 1))
                # right
                if (curr[1] + 1 < len(heights[0]) and heights[curr[0]][curr[1] + 1] >= heights[curr[0]][curr[1]] and not (curr[0], curr[1] + 1) in seen):
                    seen.add((curr[0], curr[1] + 1))
                    stack.append((curr[0], curr[1] + 1))

        # pacific iteration
        for i in range(len(heights[0])):
            dfshelp(0, i, pacific)
        for j in range(len(heights)):
            dfshelp(j, 0, pacific)
        # atlantic iteration
        for i in range(len(heights[0])):
            dfshelp(len(heights) - 1, i, atlantic)
        for j in range(len(heights)):
            dfshelp(j, len(heights[0]) - 1, atlantic)
        intersect = pacific.intersection(atlantic)
        for tup in intersect:
            ret.append([tup[0], tup[1]])
        return ret
