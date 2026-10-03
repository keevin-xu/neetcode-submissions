class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def help(idx, target, l):
            if target == 0:

# since you are only using a single list l that all 
# recursive call WORK ON, you must save the SNAPSHOT OF L
# when you append to out.
                out.append(l.copy())
                return
            for i in range(idx, len(nums)):
                if (target - nums[i] < 0):
                    continue
                l.append(nums[i])
                help(i, target-nums[i], l)
                l.pop()
        
        help(0, target, [])
        return out