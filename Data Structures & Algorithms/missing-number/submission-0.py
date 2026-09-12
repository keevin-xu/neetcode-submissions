class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum += i
        target = 0
        for j in range(len(nums) + 1):
            target += j
        return target - sum