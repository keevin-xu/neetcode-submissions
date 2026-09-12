class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = dict()
        for pre in prerequisites:
            if pre[1] not in prereqs:
                prereqs[pre[1]] = []
            prereqs[pre[1]].append(pre[0])
        seen = set()
        def help(start):
            visiting = set()
            visiting.add(start)
            tovisit = [[start, 0]]

            while tovisit:
                curr, idx = tovisit[-1]
                if curr not in prereqs:
                    tovisit.pop()
                    visiting.remove(curr)
                    seen.add(curr)
                    continue
                if idx >= len(prereqs[curr]):
                    visiting.remove(curr)
                    seen.add(curr)
                    tovisit.pop()
                else:
                    if prereqs[curr][idx] in visiting:
                        return False
                    tovisit[-1][1] += 1
                    n = prereqs[curr][idx]
                    if n not in seen and n in prereqs:    
                        tovisit.append([prereqs[curr][idx], 0])
                        visiting.add(prereqs[curr][idx])
            return True
        for j in range(numCourses):
            if not help(j):
                return False
        return True