class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        i = 0
        j = 0
        islands = 0
        seen = set()

        def travhelp(x, y):
            q = deque()
            q.append((x, y))
            while q:
                coord = q.popleft()
# above
                if (coord[0] - 1 >= 0 and grid[coord[0] - 1][coord[1]] == "1" and not (coord[0] - 1, coord[1]) in seen):
                    q.append((coord[0] - 1, coord[1]))
                    seen.add((coord[0] - 1, coord[1]))
# below
                if (coord[0] + 1 < len(grid) and grid[coord[0] + 1][coord[1]] == "1" and not (coord[0] + 1, coord[1]) in seen):
                    q.append((coord[0] + 1, coord[1]))
                    seen.add((coord[0] + 1, coord[1]))
# left
                if (coord[1] - 1 >= 0 and grid[coord[0]][coord[1] - 1] == "1" and not (coord[0], coord[1] - 1) in seen):
                    q.append((coord[0], coord[1] - 1))
                    seen.add((coord[0], coord[1] - 1))
# right
                if (coord[1] + 1 < len(grid[0]) and grid[coord[0]][coord[1] + 1] == "1" and not (coord[0], coord[1] + 1) in seen):
                    q.append((coord[0], coord[1] + 1))
                    seen.add((coord[0], coord[1] + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i, j) in seen:
                    islands += 1
                    travhelp(i, j)
        
        return islands
