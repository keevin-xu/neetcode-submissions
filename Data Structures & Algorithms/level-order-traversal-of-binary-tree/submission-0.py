# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root == None):
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            x = q.popleft()
            if x[0].left:
                q.append((x[0].left, x[1] + 1))
            if x[0].right:
                q.append((x[0].right, x[1] + 1))
            if x[1] + 1 > len(res):
                res.append([])
            res[x[1]].append(x[0].val)
        return res
            

