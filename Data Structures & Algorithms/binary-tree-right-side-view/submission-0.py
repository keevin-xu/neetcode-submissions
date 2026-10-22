# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        covered = []
        def help(node, l):
            if not node:
                return
            if l > len(covered):
                covered.append(node.val)
            help(node.right, l+1)
            help(node.left, l+1)
        help(root, 1)
        return covered