class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                s = 0
                if text1[i] == text2[j]:
                    s += 1
                if s > 0:
                    if i > 0 and j > 0:
                        s += dp[i-1][j-1]
                else:
                    s = max((dp[i-1][j] if i > 0 else 0), (dp[i][j - 1] if j > 0 else 0))
                dp[i][j] = s
        return dp[len(text1)-1][len(text2)-1]