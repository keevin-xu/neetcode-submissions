class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        links = defaultdict(list)
        for l in edges:
            links[l[0]].append(l[1])
            links[l[1]].append(l[0])

        seen = set()
        visiting = set()
        visiting.add(0)
        tovisit = [[0,0,-1]]
        while tovisit:
            curr, idx, ances = tovisit[-1]
            if idx >= len(links[curr]):
                seen.add(curr)
                visiting.remove(curr)
                tovisit.pop()
            else:
                nxt = links[curr][idx]
                if nxt in visiting and not nxt == ances:
                    return False
                tovisit[-1][1] += 1
                if not nxt == ances:
                    visiting.add(nxt)
                    tovisit.append([nxt,0,curr])
        if not len(seen) == n:
            return False
        return True