# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(node, left, right) -> bool:
            if not node:
                return True
            if not (left < node.val and node.val < right):
                return False
            else:
                return help(node.left, left, node.val) and help(node.right, node.val, right)
        return help(root, float("-inf"), float("inf"))