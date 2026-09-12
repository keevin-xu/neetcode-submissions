class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        out = nums[0]
        loc = nums[0]

        # in case all numbers are negative
        m = nums[0]
        pos = False
        if nums[0] > 0:
            pos = True
        for i in range(1, len(nums)):
            if nums[0] > 0:
                pos = True
            if loc > out:
                out = loc
            if nums[i] > m:
                m = nums[i]
            if (nums[i] + loc) < 0:
                loc = 0
            else:
                loc += nums[i]

        if not pos:
            return m
        return max(out, loc)