class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = str(len(strs)) + "*"
        for s in strs:
            ret = ret + str(len(s)) + "*"
        for s in strs:
            ret = ret + s
        return ret
    def decode(self, s: str) -> List[str]:
        if s[0] == "0":
            return []
        ret = []
        strlengths = []
        l = 0
        r = 0
        numstrings = 0
        while not s[r] == "*":
            r = r + 1
        numstrings = int(s[l:r])
        r = r + 1
        l = r
        for i in range(numstrings):
            while (not s[r] == "*"):
                r = r + 1
            strlengths.append(int(s[l:r]))
            r = r + 1
            l = r
    # r is already at the first char of the first word
        l = r
        for num in strlengths:
            ret.append(s[l:(l+num)])
            l = l + num
        return ret
        
        # find num strings
# Encoding: Prefix the concatenated string payload with a header containing the total count of strings and each individual string's length, separated by a delimiter (e.g., count*len1*len2*...*string1string2...).Decoding: Read the header to extract the number of strings and their exact lengths, then slice the remaining payload sequentially to reconstruct the original strings.Complexity: Runs in $O(m + n)$ time and space, efficiently handling special characters and empty strings without delimiter collisions.