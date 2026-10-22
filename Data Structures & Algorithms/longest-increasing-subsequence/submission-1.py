class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = longest subsequence from 0:i
        # REMEMBER: dp[i] might not hold the longest one since it has to include nums[i]!!!!
        # store the highest value you need to compare against
        dp = []
        # store initial highest value, and subsequence length
        dp.append((1,nums[0]))
        out = 1
        # remember to use a global max var!
        for i in range(1,len(nums)):
            # initial case, assume its 
            best = (1,nums[i])
            for j in range(i):
                currlen, currhigh = dp[j]
                if nums[i] > currhigh:
                    best = max(best, (currlen + 1, nums[i]))
            dp.append(best)
            out = max(out, best[0])
        return out
        