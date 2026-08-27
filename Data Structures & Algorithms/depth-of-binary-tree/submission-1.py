# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def help(node, c):
            if not node:
                return c
            return max(help(node.left, c+1), help(node.right, c+1))
        return help(root, 0)