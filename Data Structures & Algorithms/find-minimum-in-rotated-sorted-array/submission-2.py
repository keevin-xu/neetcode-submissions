class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = (len(nums) - 0) // 2
        l = 0
        r = len(nums) - 1
        while (l != m):
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
            m = (r - l) // 2 + l
        return min(nums[m], nums[r])