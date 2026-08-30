# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(p, q):
            def equalh(x, y):
                if not x and not y:
                    return True
                if not x and y or x and not y:
                    return False
                if x.val != y.val:
                    return False
                return equalh(x.left, y.left) and equalh(x.right, y.right)
            return equalh(p, q)
        def help(p, q):
            if not p:
                return False
            if (equal(p, q)):
                return True
            return help(p.left, q) or help(p.right, q)
        return help(root, subRoot)