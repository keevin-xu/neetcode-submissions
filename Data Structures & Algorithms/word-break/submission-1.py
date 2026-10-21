class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * len(s)
        for i in range(len(dp)):
            success = False
            for x in wordDict:
                dpInd = i - len(x)

                # if dpInd should be True. this is the case where you haven't found a word before yet.
                if dpInd < -1:
                    continue
                if dpInd == -1 or dp[dpInd] == True:
                    if s[dpInd+1:i+1] == x:
                        success = True
            dp[i] = success
        return dp[-1]