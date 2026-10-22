from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = ['*'] * len(graph)
        def bfs(i, color):
            if not colors[i] == '*':
                return True
            queue = deque()
            queue.append((i,color))
            while queue:    
                curr = queue.popleft()
                colors[curr[0]] = curr[1]
                for j in graph[curr[0]]:
                    if colors[j] == '*':
                        queue.append((j, not curr[1]))
                    elif colors[j] == curr[1]:
                        return False
            
            return True

        for i in range(len(graph)):
            if colors[i] == '*':
                if not bfs(i, True):
                    return False
        return True