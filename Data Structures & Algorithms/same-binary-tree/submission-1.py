# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def help(p, q):
            if not p and not q:
                return True
            if not p and q or p and not q:
                return False
            if p.val != q.val:
                return False
            return help(p.left, q.left) and help(p.right, q.right)
        return help(p, q)