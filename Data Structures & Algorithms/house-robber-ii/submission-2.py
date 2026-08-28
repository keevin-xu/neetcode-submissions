class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        m = nums.copy()
        m[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            m[i] = max(m[i-2] + m[i], m[i-1])
            print(m[2])
        x = m[len(nums) - 2]

        m = nums.copy()
        m[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            m[i] = max(m[i-2] + m[i], m[i-1])
        print(m[len(nums) - 1])
        return max(x, m[len(nums) - 1])