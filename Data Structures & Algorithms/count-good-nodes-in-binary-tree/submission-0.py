# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#float('-inf')
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def help(node, val):
            if not node:
                return
            if node.val >= val:
                count[0] += 1
            help(node.left, max(val, node.val))
            help(node.right, max(val, node.val))
        help(root, float('-inf'))
        return count[0]
