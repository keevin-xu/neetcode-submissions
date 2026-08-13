class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        bestI = 0
        minI = 0
        for i in range(1, len(prices)):
            if (prices[i] - prices[bestI]) > best:
                best = prices[i] - prices[bestI]
            if (prices[i] - prices[minI] > best):
                best = prices[i] - prices[minI]
            if (prices[i] < prices[minI]):
                minI = i
        return best