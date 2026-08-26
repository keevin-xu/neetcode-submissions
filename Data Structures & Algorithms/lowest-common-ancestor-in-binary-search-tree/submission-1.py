# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = p.val
        right = q.val
        x = root
        if p.val > q.val:
            right = p.val
            left = q.val
        while (True):
            if x.val == left or x.val == right:
                return x
            if x.val > left and x.val > right:
                x = x.left
            elif x.val < left and x.val < right:
                x = x.right
            else:
                return x

