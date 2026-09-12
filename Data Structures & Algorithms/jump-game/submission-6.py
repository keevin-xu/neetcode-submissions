class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
#            print(i)
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            m = nums[i] if i + nums[i] < len(nums) else len(nums) - 1 - i
            for j in range(1, nums[i] + 1):
                if ((i + j) < len(nums) and nums[i + j] >= nums[i + m] and ((i+j) + nums[i+j]) > (nums[i] + i)):
                    m = j
                    
            if i + nums[i] >= len(nums) - 1:
                return True
            i += m       
        return True