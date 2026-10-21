# recursive implementation. 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use a set for already verified nodes that have no cycle. to optimize.
        verified = set()
        
        
        # only if there is no cycle
        prereqs = dict()
        for i in range(numCourses):
            prereqs[i] = []
        for pre in prerequisites:
            prereqs[pre[1]].append(pre[0])
        
        seen = set()
        def cycle(i):
            # check against the verified set
            if i in verified:
                return False

            if not prereqs[i]:
                verified.add(i)
                return False
            if i in seen:
                return True
            seen.add(i)
            ret = False
            for j in prereqs[i]:
                if cycle(j):
                    ret = True
            seen.remove(i)
            if not ret:
                verified.add(i)
            return ret

        for i in range(numCourses):
            if cycle(i):
                return False
        return True