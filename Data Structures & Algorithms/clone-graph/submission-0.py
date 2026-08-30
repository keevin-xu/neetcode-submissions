"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = dict()
        seen = set()
        seen.add(node)
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            if not curr in nodes:
                nodes[curr] = Node(curr.val, [])
            for nei in curr.neighbors:
                if not nei in nodes:
                    nodes[nei] = Node(nei.val, [])
                if not nei in seen:
                    q.append(nei)
                    seen.add(nei)
                nodes[curr].neighbors.append(nodes[nei])
        return nodes[node]

