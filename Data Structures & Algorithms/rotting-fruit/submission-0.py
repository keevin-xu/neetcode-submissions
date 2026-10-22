from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

# bfs from multiple starting points. just add all starting points to the beginning queue.
# initial pass for num fruits. when num fruits hits zero record the length
# return 0 immediately if remaining num fruits is zero after first pass.
# returning -1 if after queue is empty, there are still fruits left over (unreachable fruits)
        queue = deque()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        level = 0
        while queue:
            r,c,l = queue.popleft()
            if (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (r,c) not in seen and (grid[r][c] == 1 or grid[r][c] == 2)):
                seen.add((r,c))
                level = l
                queue.append((r-1,c,l+1))
                queue.append((r+1,c,l+1))
                queue.append((r,c+1,l+1))
                queue.append((r,c-1,l+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    return -1
        return level