from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        d = defaultdict(int)
        freq = 0
        i = 0
        for j in range(len(s)):
            d[s[j]] += 1
            freq = max(freq, d[s[j]])
            if (j - i + 1 - freq > k):
                d[s[i]] -= 1
                i += 1
            if (j - i + 1) > ans:
                ans = j - i + 1
        return ans