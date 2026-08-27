# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map = dict()
        for i in range(len(inorder)):
            map[inorder[i]] = i
        preind = [0]
        def help(l, r):
            if l >= r:
                return None
            piv = map[preorder[preind[0]]]
            rootval = preorder[preind[0]]
            preind[0] = preind[0] + 1
            return TreeNode(rootval, help(l, piv), help(piv + 1, r))
        return help(0, len(inorder))