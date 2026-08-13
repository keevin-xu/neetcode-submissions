class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)) == 0:
            return 0
        i = 0
        j = 0
        best = 1
        poop = set()
        while j < len(s):
            if s[j] not in poop:
                poop.add(s[j])
                j += 1
            else:
                if (j - i) > best:
                    best = j - i
                poop.remove(s[i])
                i += 1
        if (j - i) > best:
            best = j - i
        return best
