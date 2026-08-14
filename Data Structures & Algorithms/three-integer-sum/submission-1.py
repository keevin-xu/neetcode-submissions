class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        j = i+1
        k = len(nums) - 1
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums) - 1
            j = i + 1
            while (j < k):
                if (nums[j] + nums[k] + nums[i]) > 0:
                    k -= 1
                elif (nums[j] + nums[k] + nums[i]) < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1

                    k -= 1
                    j += 1
        return ans