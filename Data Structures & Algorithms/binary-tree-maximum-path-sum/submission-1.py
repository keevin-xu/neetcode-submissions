# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dp[node] = max sum with node as the top of the upsidedown V path

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = [root.val]
        def dfs(node):
            if not node:
                return 0
            leftmax = max(0, dfs(node.left))
            rightmax = max(0, dfs(node.right))
            
            ret[0] = max(ret[0], node.val + leftmax + rightmax)
            return node.val + max(leftmax, rightmax)
        dfs(root)
        return ret[0]