class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = (len(nums) - 0) // 2
        l = 0
        r = len(nums) - 1
        while (l != m):
            if nums[l] < nums[m] < nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m
            elif nums[r] < nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m
            
            # nums[m] < nums[r] < nums[l]
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m


            m = (r - l) // 2 + l
        if (nums[m] == target):
            return m
        elif (nums[r] == target):
            return r
        return -1