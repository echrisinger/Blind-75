# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p
        
        curr = root
        lesser, greater = (p, q) if p.val < q.val else (q, p)
        
        while not (curr.val >= lesser.val and curr.val <= greater.val):
            if curr.val > greater.val:
                curr = curr.left
            else:
                curr = curr.right
                
        return curr

