from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = defaultdict(int)
        ret = ""
        ind = [0, 1]
        for i in range(len(t)):
            map[t[i]] += 1
        
        need = len(map)
        have = 0
        
        curr = defaultdict(int)
        i = 0
        j = 0
        while (j < len(s)):
            if s[j] in map:
                curr[s[j]] += 1
                if curr[s[j]] == map[s[j]]:
                    have += 1
            while need == have:
                if (j-i+1) < len(ret) or ret == "":
                    ret = s[i:j+1]
                if s[i] in map:
                    curr[s[i]] -= 1
                    if curr[s[i]] < map[s[i]]:
                        have -= 1
                i += 1
            j += 1
        print(curr)
        return ret