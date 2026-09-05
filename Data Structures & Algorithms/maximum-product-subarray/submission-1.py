class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totalmax = nums[0]
        localmax = nums[0]
        localmin = nums[0]

        for i in range(1, len(nums)):
            currmax = localmax
            localmax = max(nums[i], localmax * nums[i], localmin * nums[i])

            # use curr max so you are using the correct localmax (the one from the previous element)
            # you don't want to use the localmax you just updated
            localmin = min(nums[i], currmax * nums[i], localmin * nums[i])

            if localmax > totalmax:
                totalmax = localmax

        return totalmax

        