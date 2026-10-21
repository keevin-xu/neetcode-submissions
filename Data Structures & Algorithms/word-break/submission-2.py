class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        # invariant: dp[i] means if s[0: up to i EXCLUSIVE] can be made from dict.
        # that's why you need len(s)
        for i in range(1, len(s) + 1):
            for j in range(i):
                # if dp[j] checks if the prefix up to j can be made from dict.
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]