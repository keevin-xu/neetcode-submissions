class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letters = [0] * 26
        for x in range(len(s)):
            letters[ord(s[x]) - 97] += 1
            letters[ord(t[x]) - 97] -= 1
        for x in letters:
            if x != 0:
                return False
        return True