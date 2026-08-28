class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        ret = nums.copy()
        for i in range(len(nums)):
            ret[i] = l
            l = l * nums[i]
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = ret[i] * r
            r = r * nums[i]
        return ret
# prefix and suffix sum
# two separate passes.
# prefix pass each element equals the product of the elemnts to the left.
# suffix pass multiply the existing prefix value by the running product of elements to its right. multiply the prefix array with your running SUFFIX TOTAL INT.
# will converge once both passes are done. each element will be the product of the others.
# keep the input array as is so you still have access to the correct values to multiply by
# 