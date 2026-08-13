class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, x in enumerate(nums):
            map[x] = index
        for index, x in enumerate(nums):
            if target - x in map and map[target - x] != index:
                return [index, map[target-x]]