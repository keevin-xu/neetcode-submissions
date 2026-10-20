from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0

        def dfs(i,j):
            stack = []
            stack.append((i,j))

            while stack:
                curr = stack.pop()
                if curr[0] >= 0 and curr[0] < (len(grid)) and curr[1] >= 0 and curr[1] < len(grid[0]) and grid[curr[0]][curr[1]] == '1':
                    grid[curr[0]][curr[1]] = '0'
                    stack.append((curr[0]-1,curr[1]))
                    stack.append((curr[0]+1,curr[1]))
                    stack.append((curr[0],curr[1]-1))
                    stack.append((curr[0],curr[1]+1))

        # outer loop

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    out += 1
        return out