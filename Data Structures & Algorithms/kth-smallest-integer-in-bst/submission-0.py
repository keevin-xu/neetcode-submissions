# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def help(node):
            if len(l) >= k:
                return l[k - 1]
            if not node:
                return;
            help(node.left)
            l.append(node.val)
            help(node.right)
        help(root)
        return l[k-1]
