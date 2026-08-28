class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        l = 0
        r = 0
        for i in range(len(s)):
            l = i
            r = i
            while (s[l] == s[r]):
                ret = ret + 1
                l -= 1
                r += 1
                if l < 0 or r >= len(s):
                    break
    # check if l and r hit bounds of string
            if (i < len(s) - 1):
                l = i
                r = i + 1
                while (s[l] == s[r]):
                    ret = ret + 1
                    l -= 1
                    r += 1
                    if l < 0 or r >= len(s):
                        break
        return ret