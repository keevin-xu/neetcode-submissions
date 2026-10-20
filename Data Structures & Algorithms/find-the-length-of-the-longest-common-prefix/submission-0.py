class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixSet = set()
        for a in arr1:
            c = ""
            aword = str(a)
            for char in aword:
                c += char
                prefixSet.add(c)
        out = 0
        for b in arr2:
            x = ""
            bword = str(b)
            for char in bword:
                x += char
                if x in prefixSet:
                    out = max(out, len(x))
        return out
