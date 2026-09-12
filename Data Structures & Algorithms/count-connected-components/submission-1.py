class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        out = 0
        seen = set()

        links = defaultdict(list)
        for l in edges:
            links[l[0]].append(l[1])
            links[l[1]].append(l[0])

        def help(j):
            tovisit = [j]
            while tovisit:
                curr = tovisit.pop()
                for n in links[curr]:
                    if n not in seen:
                        tovisit.append(n)
                seen.add(curr)

        for i in range(n):
            if i not in seen:
                out += 1
                help(i)
        return out