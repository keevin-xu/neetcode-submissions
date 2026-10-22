# does not work
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = set()
        ret = []
        curr = []
        def back(n):

            if n in current:
                return
            curr.append(n)
            current.add(n)
            if len(curr) == len(nums):
                ret.append(curr.copy())
            for i in nums:
                back(i)
            curr.pop()
            current.remove(n)
        for j in nums:
            back(j)
        return ret