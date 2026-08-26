from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = defaultdict(int)
        for i in nums:
            x[i] = x[i] + 1


        y = [set() for _ in range(len(nums) + 1)]

        for key, val in x.items():
            y[val].add(key)
        
        j = len(y) - 1
        res = []
        var = k
        while (var > 0):
            if not y[j]:
                j = j - 1
                continue
            else:
                res.append(y[j].pop())
                var = var - 1
        return res