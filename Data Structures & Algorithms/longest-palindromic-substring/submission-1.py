class Solution:
    def longestPalindrome(self, s: str) -> str:
        outLen = 1
        currLen = 1
        currOut = 0
        out = 0
        i = 0

# helper pointers         
        j = 0
        k = 0
        while (i < len(s) - 1):
            if (s[i] == s[i + 1]):
                j = i
                k = i + 1
                currLen = 0
                while (j >= 0 and k < len(s)):
                    if (s[j] == s[k]):
                        currOut = j
                        j = j - 1
                        k = k + 1
                        currLen = currLen + 2
                    else:
                        break
                if currLen > outLen:
                    outLen = currLen
                    out = currOut
            
            j = i - 1
            k = i + 1
            currLen = 1                
            while (j >= 0 and k < len(s)):
                if (s[j] == s[k]):
                    currOut = j
                    j = j - 1
                    k = k + 1
                    currLen = currLen + 2
                else:
                    break
            if currLen > outLen:
                outLen = currLen
                out = currOut
            i = i + 1
        return s[out:(out+outLen)]




# abbad